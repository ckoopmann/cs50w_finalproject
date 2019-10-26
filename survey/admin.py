from django.contrib import admin
from .models import Survey, SurveyOption, Vote

admin.site.register(Survey)
admin.site.register(SurveyOption)
admin.site.register(Vote)
