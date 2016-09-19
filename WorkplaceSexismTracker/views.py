from django.shortcuts import render
from django.http import HttpResponse
from models import Event

def index(request):
    events = Event.objects.all()
    event1desc = events[0].event_description
    return HttpResponse(event1desc)
#    return render(request, 'test.html')
