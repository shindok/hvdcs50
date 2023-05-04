from django.shortcuts import render, redirect
from .models import Task
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['created_by', 'completed_at']


@login_required
def index(request):
    user = request.user
    tasks_assigned_to_user = Task.objects.filter(assigned_to=user)
    tasks_created_by_user = Task.objects.filter(created_by=user)
    tasks = tasks_assigned_to_user | tasks_created_by_user
    return render(request, "tasks/index.html", {
        "tasks" : tasks
    })


@login_required
def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.created_by = request.user
            task.save()
            messages.success(request, "Task added successfully")
            return redirect("tasks:index")
    else:
        form = TaskForm()
    return render(request, "tasks/add.html", {"form": form})
