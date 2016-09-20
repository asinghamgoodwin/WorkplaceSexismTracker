from django import forms
from django.forms import ModelForm
from django.forms import widgets
from .models import Event, User, Category

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['event_date', 'event_people', 
                    'event_private_yesno', 'event_description', 
                    'event_immediate_response_yesno', 
                    'event_reaction', 'event_category', 
                    'event_cost_rating', 'event_cost_desc', 
                    ]

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=widgets.PasswordInput())

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'

