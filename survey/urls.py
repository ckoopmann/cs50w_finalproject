from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='survey-home'),
    path('about/', views.about, name='survey-about')
]
