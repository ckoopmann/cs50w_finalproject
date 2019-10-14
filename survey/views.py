from django.shortcuts import render

messages = ['Welcome to Djoodle from the template!',
        'So Welcome']
title = 'Test'
def home(request):
    context = {
            'messages': messages,
            'title': title
    }
    return render(request, 'survey/home.html', context)
