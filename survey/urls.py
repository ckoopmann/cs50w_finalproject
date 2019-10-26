from django.urls import path
from .views import SurveyDetailView, SurveyListView

urlpatterns = [
    path('', SurveyListView.as_view(), name='survey-home'),
    path('survey/<int:pk>', SurveyDetailView.as_view(), name='survey-detail'),
]
