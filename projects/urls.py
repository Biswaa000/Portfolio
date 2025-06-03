from . import views
from django.urls import path,include 

urlpatterns = [
    path('projects/', views.projects_list, name='projects_list'),
    path('projects/add/', views.project_add, name='project_add'),
    path('projects/<int:pk>/edit/', views.project_edit, name='project_edit'),
    path('projects/<int:pk>/delete/', views.project_delete, name='project_delete'),
    
]

