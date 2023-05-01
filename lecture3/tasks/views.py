from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Task


# Create your views here.
<<<<<<< HEAD


def index(request):

    tasks = Task.objects.all();

    return render(request, "tasks/index.html", {"tasks": tasks})

def add_task(request):

    return render(request, "tasks/add.html")
=======
# tasks = []

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

def add(request):
    # serverside validation
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"]+=[task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {"form": form})
    return render(request, "tasks/add.html", {"form": NewTaskForm()})
>>>>>>> main
