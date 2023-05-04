from django.contrib import admin
from .models import Status, Task, Project

# Register your models here.

admin.site.register(Status)
admin.site.register(Task)
admin.site.register(Project)