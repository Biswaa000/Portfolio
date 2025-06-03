from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import Project
from .forms import ProjectForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView

def projects_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/projects_list.html', {'projects': projects})

@login_required(login_url=reverse_lazy('account_login'))  # Update with your login URL
def project_add(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user  # Associate project with current user
            project.save()
            messages.success(request, 'Project added successfully!')
            return redirect('projects_list')
    else:
        form = ProjectForm()
    
    return render(request, 'projects/project_form.html', {'form': form})

@login_required(login_url=reverse_lazy('account_login'))
def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    
    # Check if current user owns the project
    if project.user != request.user:
        messages.error(request, "You don't have permission to edit this project.")
        return redirect('projects_list')
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project updated successfully!')
            return redirect('projects_list')
    else:
        form = ProjectForm(instance=project)
    
    return render(request, 'projects/project_edit.html', {
        'form': form,
        'project': project
    })

@login_required(login_url=reverse_lazy('account_login'))
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    
    # Check if current user owns the project
    if project.user != request.user:
        messages.error(request, "You don't have permission to delete this project.")
        return redirect('projects_list')
    
    if request.method == 'POST':
        project.delete()
        messages.success(request, 'Project deleted successfully!')
        return redirect('projects_list')
    
    return render(request, 'projects/project_confirm_delete.html', {'project': project})