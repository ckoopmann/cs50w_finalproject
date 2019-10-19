from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Survey(models.Model):
    title = models.CharField(max_length=30) 
    description = models.CharField(max_length=300) 
    date_created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return f'Title: {self.title}, Author: {self.author}'
