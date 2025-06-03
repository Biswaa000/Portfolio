from django.urls import path,include
from . import views


urlpatterns = [
    path('login/', views.user_login, name='account_login'),
    path('logout/', views.user_logout, name='account_logout'),
    path('dashboard/', views.dashboard, name='account_dashboard'),
    # path('admin/', include('account.urls')),
]