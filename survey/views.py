from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView)
from .models import Survey, SurveyOption, Vote
from .forms import VoteForm

def home(request):

    if request.user.is_authenticated:
        return redirect('survey-list')

    return render(request, "survey/about.html")


class SurveyListView(ListView):
    model = Survey
    template_name = 'survey/home.html'
    context_object_name = 'surveys'
    ordering = ['-date_created']
    
    def get_queryset(self):
        return Survey.objects.raw(f'SELECT * FROM survey_survey WHERE author_id={self.request.user.id}')

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


class VoteCreateView(CreateView):
    form_class = VoteForm
    model = Vote

    def get_success_url(self):
            return reverse('survey-detail', kwargs={'pk': self.kwargs['pk']})

    def get_form_kwargs(self):
            kwargs = super(VoteCreateView, self).get_form_kwargs()
            kwargs.update({'pk': self.kwargs.get('pk')})
            return kwargs

    def get_context_data(self, **kwargs):
        ctx = super(VoteCreateView, self).get_context_data(**kwargs)
        ctx['survey'] = Survey.objects.get(pk=self.kwargs['pk'])
        return ctx

class VoteListView(ListView):
    model = Vote
    context_object_name = 'votes'
    ordering = ['-date_created']
    
    def get_context_data(self, **kwargs):
        ctx = super(VoteListView, self).get_context_data(**kwargs)
        surveyoption =  SurveyOption.objects.get(pk=self.kwargs['pk'])
        ctx['surveyoption'] = surveyoption
        ctx['survey'] = surveyoption.survey
        return ctx

    def get_queryset(self):
        return Vote.objects.filter(survey_option=self.kwargs.get('pk'))

class VoteDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Vote

    def test_func(self):
        vote = self.get_object()
        survey_option = vote.survey_option
        survey = survey_option.survey
        if self.request.user == survey.author:
            return True
        else:
            return False

    def get_success_url(self):
        vote = self.get_object()
        survey_option = vote.survey_option
        return reverse('vote-list', kwargs={'pk': survey_option.id})


