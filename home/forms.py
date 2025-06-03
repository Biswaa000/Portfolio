from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control bg-transparent text-white',
        'placeholder': 'Your Name'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control bg-transparent text-white',
        'placeholder': 'Your Email'
    }))
    subject = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control bg-transparent text-white',
        'placeholder': 'Subject'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control bg-transparent text-white',
        'placeholder': 'Your Message',
        'rows': 5
    }))
    