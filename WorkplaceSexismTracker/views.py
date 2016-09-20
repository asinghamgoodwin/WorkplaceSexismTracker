from django.shortcuts import render
from django.http import HttpResponse
from models import Event
from forms import EventForm, UserForm, LoginForm

def index(request):
    events = Event.objects.all()
    event1desc = events[0].event_description
    return HttpResponse("this is just a test that things are linked up to a database: "+event1desc)
    # pass to login page instead?

def login(request):
    form = LoginForm()
    return render(request, 'login.html', {'form':form})

def acceptLogin(request):
    pass

def newUser(request):
    form = UserForm()
    return render(request, 'newUser.html', {'form':form})

def userCreated(request):
    pass

def newEvent(request):
    form = EventForm()
    return render(request, 'newEvent.html', {'form':form})

def eventCreated(request):
    if request.POST:
        desc = request.POST['event_description']

        newEvent = Event(event_description=desc)
        newEvent.save()

        events = Event.objects.all()
        descList = [event.event_description for event in events]
        lastDesc = descList[-1]
        return HttpResponse(lastDesc)
    else: return HttpResponse("failed")
