from django.db import models

# Create your models here.
class Task(models.Model):
    task=models.TextField(max_length=200,null=True)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
