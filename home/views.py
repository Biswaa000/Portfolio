
from django.shortcuts import HttpResponse
from projects.models import  Project
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.cache import cache
from django.contrib import messages



# Create your views here.
def home(request):
    context = {
        'name' : 'Bishal Sharma',
        'title' : "Home",
        'email' : "bishalsharma406365@gmail.com",
        'phone' : "+9779817786631",
        'location' : "Dharan, Nepal"    ,
        'projects' : Project.objects.order_by('-created_at')[:3]


    }
    return render(request,'home/home.html',context)

def about_me(request):
    context = {
        'name' : 'Bishal Sharma',
        'title' : "Home"
     }
    return render(request,'home/about_me.html',context)

def test(request):
    return render(request,'home/test.html')






def get_client_ip(request):
    """Utility to get client IP address, accounting for proxies"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def contact_view(request):
    ip = get_client_ip(request)
    blocked = cache.get(f"block_{ip}")

    if blocked:
        messages.warning(request,"⚠️ You're sending messages too quickly. Please wait 30 seconds and try again.")
        return redirect(home)
        # return HttpResponse("⚠️ You're sending messages too quickly. Please wait 30 seconds and try again.", status=429)

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject'] or 'No Subject'
            message = form.cleaned_data['message']

            try:
                # Set temporary block (30 seconds)
                cache.set(f"block_{ip}", True, timeout=30)

                # Email to you
                send_mail(
                    subject=f"New Contact: {subject}",
                    message=f"From: {name} <{email}>\n\nMessage:\n{message}",
                    from_email='bishalsharma406366@gmail.com',
                    recipient_list=['bishalsharma406365@gmail.com'],
                    fail_silently=False,
                )

                # Confirmation to user
                send_mail(
                    subject="Thanks for contacting me!",
                    message="Hello! 👋\n\nThank you for reaching out. I’ll get back to you soon.\n\nRegards,\nBiswaa",
                    from_email='bishalsharma406366@gmail.com',
                    recipient_list=[email],
                    fail_silently=False,
                )

                return redirect('contact_success')

            except BadHeaderError:
                return HttpResponse("Invalid header found.", status=400)

    else:
        form = ContactForm()

    return render(request, 'home/home.html', {'form': form})


def contact_success(request):
    messages.success(request, 'Your message has been sent successfully!')
    return redirect('home')
