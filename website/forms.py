from django import forms

from .models import Submission
from .models import Again

class SubmissionForm(forms.ModelForm):

    class Meta:
        model = Submission
        fields = ('prolific_id', 'spoofer_URL',)

class AgainForm(forms.ModelForm):

    class Meta:
        model = Again
        fields = ('prolific_id',)