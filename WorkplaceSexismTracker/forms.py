from django import forms
from .models import Event, User, Category

class EventForm(forms.Form):
    event_description = forms.CharField(max_length=500)


class LoginForm(forms.Form):
    pass


class UserForm(forms.Form):
    pass
