from django.shortcuts import render
from .models import Task
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    #clientside validation
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
        })

def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            # TODO: task.creator = request.user
            task.save()
            return redirect("tasks:index") # TODO: include success message
        else:
            form = TaskForm()
    return render(request, "tasks/add.html")