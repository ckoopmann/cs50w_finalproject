from django.urls import path
from .views import (
        SurveyCreateView,
        SurveyDeleteView,
        SurveyDetailView,
        SurveyListView,
        SurveyOptionCreateView,
        SurveyOptionDeleteView,
        SurveyUpdateView,
        VoteCreateView
)

urlpatterns = [
    path('', SurveyListView.as_view(), name='survey-home'),
    path('survey/new/', SurveyCreateView.as_view(), name='survey-create'),
    path('survey/<int:pk>/newoption/', SurveyOptionCreateView.as_view(), name='surveyoption-create'),
    path('survey/<int:pk>/', SurveyDetailView.as_view(), name='survey-detail'),
    path('survey/<int:pk>/update/', SurveyUpdateView.as_view(), name='survey-update'),
    path('survey/<int:pk>/delete/', SurveyDeleteView.as_view(), name='survey-delete'),
    path('survey/<int:pk>/newvote/', VoteCreateView.as_view(), name='vote-create'),
    path('survey/deleteoption/<int:pk>/', SurveyOptionDeleteView.as_view(), name='surveyoption-delete'),
]
