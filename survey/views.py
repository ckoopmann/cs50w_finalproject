from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Survey

class SurveyListView(ListView):
    model = Survey
    template_name = 'survey/home.html'
    context_object_name = 'surveys'
    ordering = ['-date_created']

class SurveyDetailView(DetailView):
    model = Survey
