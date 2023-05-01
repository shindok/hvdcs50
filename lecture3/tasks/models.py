from django.db import models

# Create your models here.
# [complete, incomplete, tabled]
class Status(models.Model):
    #id(objects.AutoField(primary_key=True)) unnecessary; generated via django
    status = models.CharField(max_length=20)


class Task(models.Model):
    description = models.CharField(max_length=100, blank=False, null=False)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, blank=False, null=False)
    detail = models.CharField(max_length=2000, blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    startTime = models.DateTimeField(auto_now_add=True, null=False)
    goalTime = models.DateTimeField(blank=True, null=True)
    endTime = models.DateTimeField(blank=True, null=True)
