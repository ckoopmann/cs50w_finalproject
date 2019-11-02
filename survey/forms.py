from django.forms import ModelForm
from .models import Survey, SurveyOption, Vote

class VoteForm(ModelForm):

    class Meta:
        model = Vote
        fields = ['voter', 'survey_option']
        labels = {'voter': 'Your Name', 'survey_option':'Your Selection'}

    def __init__(self, *args, **kwargs):
        survey_id = kwargs.pop('pk')
        super(VoteForm, self).__init__(*args, **kwargs)
        self.fields['survey_option'].queryset = Survey.objects.get(pk=survey_id).surveyoption_set
