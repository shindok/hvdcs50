from django.shortcuts import render

from .models import Task


# Create your views here.


def index(request):

    tasks = Task.objects.all();

    return render(request, "tasks/index.html", {"tasks": tasks})

def add_task(request):

    return render(request, "tasks/add.html")