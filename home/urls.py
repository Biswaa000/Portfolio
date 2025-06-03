from . import views
from django.urls import path,include 

urlpatterns = [
    
    path('',views.home,name='home1'),
    path('home/',views.home,name='home'),
    path('about_me/',views.about_me,name='about_me'),
    path('test/',views.test),
    path('contact/', views.contact_view, name='contact_view'),
    path('contact/success/', views.contact_success, name='contact_success'),

]
