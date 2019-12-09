from django import forms
from .models import Event

class PartialAuthorForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['author']
