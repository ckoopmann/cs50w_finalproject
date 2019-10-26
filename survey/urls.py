from django.urls import path
from .views import (
        SurveyCreateView,
        SurveyDeleteView,
        SurveyDetailView,
        SurveyListView,
        SurveyUpdateView
)

urlpatterns = [
    path('', SurveyListView.as_view(), name='survey-home'),
    path('survey/new/', SurveyCreateView.as_view(), name='survey-create'),
    path('survey/<int:pk>/', SurveyDetailView.as_view(), name='survey-detail'),
    path('survey/<int:pk>/update/', SurveyUpdateView.as_view(), name='survey-update'),
    path('survey/<int:pk>/delete/', SurveyDeleteView.as_view(), name='survey-delete'),
]
