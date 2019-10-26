from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Survey(models.Model):
    """A survey that can be created and shared by registered users"""
    title = models.CharField(max_length=30) 
    description = models.CharField(max_length=300) 
    date_created = models.DateTimeField(default=timezone.now)
    allow_create_new_option = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return f'Title: {self.title}, Author: {self.author}'

class SurveyOption(models.Model):
    """One available Option of a survey that can potentially be selected by anyone participating in the survey"""
    description = models.CharField(max_length=300) 
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.description}'

class Vote(models.Model):
    """A vote that has been cast for a specific option of a specific survey"""
    survey_option = models.ForeignKey(SurveyOption, on_delete=models.CASCADE)
    voter = models.CharField(max_length=30) 

    def __str__(self):
        return f'{self.voter} chose {self.survey_option.description}'
