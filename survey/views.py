from django.shortcuts import render
from .models import Survey

messages = ['Welcome to Djoodle from the template!',
        'So Welcome']
title = 'Test'
def home(request):
    context = {
            'title': title,
            'surveys': Survey.objects.all()
    }
    return render(request, 'survey/home.html', context)
