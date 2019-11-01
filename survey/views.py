from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView)
from .models import Survey, SurveyOption

class SurveyListView(ListView):
    model = Survey
    template_name = 'survey/home.html'
    context_object_name = 'surveys'
    ordering = ['-date_created']

class SurveyDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Survey
    success_url = '/'

    def test_func(self):
        survey = self.get_object()
        if self.request.user == survey.author:
            return True
        else:
            return False

class SurveyDetailView(DetailView):
    model = Survey

class SurveyCreateView(LoginRequiredMixin, CreateView):
    model = Survey
    fields = ['title','description', 'allow_create_new_option']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class SurveyUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Survey
    fields = ['title','description', 'allow_create_new_option']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        survey = self.get_object()
        if self.request.user == survey.author:
            return True
        else:
            return False


class SurveyOptionCreateView(LoginRequiredMixin, CreateView):
    model = SurveyOption
    fields = ['description']

    def form_valid(self, form):
        form.instance.survey = Survey.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
            return reverse('survey-detail', kwargs={'pk': self.kwargs['pk']})


class SurveyOptionDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = SurveyOption

    def test_func(self):
        surveyoption = self.get_object()
        if self.request.user == surveyoption.survey.author:
            return True
        else:
            return False

    def get_success_url(self):
        surveyoption = self.get_object()
        return reverse('survey-detail', kwargs={'pk': surveyoption.survey.id})



