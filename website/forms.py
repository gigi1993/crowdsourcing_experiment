from django import forms

from .models import Submission
from .models import Failed
from .models import Again

class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ('prolific_id', 'spoofer_URL',)

class FailedForm(forms.ModelForm):
    class Meta:
        model = Failed
        fields = ('prolific_id',)

class AgainForm(forms.ModelForm):
    class Meta:
        model = Again
        fields = ('prolific_id',)