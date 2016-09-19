from django import forms
from .models import Event

class EventForm(forms.Form):
    event_description = forms.CharField(max_length=500)
