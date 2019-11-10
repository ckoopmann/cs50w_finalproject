from django.urls import path
from .views import (
        home,
        SurveyCreateView,
        SurveyDeleteView,
        SurveyDetailView,
        SurveyListView,
        SurveyOptionCreateView,
        SurveyOptionDeleteView,
        SurveyUpdateView,
        VoteCreateView,
        VoteDeleteView,
        VoteListView
)

urlpatterns = [
    path('', home, name='survey-home'),
    path('survey/list/', SurveyListView.as_view(), name='survey-list'),
    path('survey/new/', SurveyCreateView.as_view(), name='survey-create'),
    path('survey/<int:pk>/newoption/', SurveyOptionCreateView.as_view(), name='surveyoption-create'),
    path('survey/<int:pk>/', SurveyDetailView.as_view(), name='survey-detail'),
    path('survey/<int:pk>/update/', SurveyUpdateView.as_view(), name='survey-update'),
    path('survey/<int:pk>/delete/', SurveyDeleteView.as_view(), name='survey-delete'),
    path('survey/<int:pk>/newvote/', VoteCreateView.as_view(), name='vote-create'),
    path('survey/deleteoption/<int:pk>/', SurveyOptionDeleteView.as_view(), name='surveyoption-delete'),
    path('survey/deletevote/<int:pk>/', VoteDeleteView.as_view(), name='vote-delete'),
    path('survey/listvotes/<int:pk>/', VoteListView.as_view(), name='vote-list'),
]
