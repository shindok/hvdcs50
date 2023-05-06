from wsgiref.validate import validator
from django.db import models
from accounts.models import CustomUser


class Status(models.Model):
    name = models.CharField(max_length=100, default="Incomplete")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Statuses"

class Project(models.Model):
    name = models.CharField(max_length=100, default="New Project")
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    started_at = models.DateTimeField(blank=True, null=True)
    completed_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.name
    
def validate_priority(value):
    if value < 1 or value > 5:
        raise ValueError("Priority must be between 1 and 5")

class Task(models.Model):
    status = models.ForeignKey(Status, on_delete=models.PROTECT, db_index=True, default="Incomplete")
    name = models.CharField(max_length=100, default="New Task")
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    due_at = models.DateTimeField(blank=True, null=True)
    started_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.PROTECT, db_index=True, blank=True, null=True)
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.PROTECT, db_index=True, blank=True, null=True,
                                    related_name='assignee')
    assigned_by = models.ForeignKey(CustomUser, on_delete=models.PROTECT, db_index=True, blank=True, null=True,
                                    related_name='assigner')
    created_by = models.ForeignKey(CustomUser, on_delete=models.PROTECT, db_index=True, related_name='creator', 
                                   null=True)
    priority = models.IntegerField(default=1, validators=[validate_priority])
    completed_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['due_at']
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    def __str__(self):
        return f"{self.status} | {self.name} | priority : {self.priority}"
