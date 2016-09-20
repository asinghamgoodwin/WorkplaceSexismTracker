from django.shortcuts import render
from django.http import HttpResponse
from models import Event, User, Category
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
    if request.POST:
        return HttpResponse('got login info from form')
    return HttpResponse("didn't get login info from form")

def newUser(request):
    form = UserForm()
    return render(request, 'newUser.html', {'form':form})

def userCreated(request):
    if request.POST:
        user_name = request.POST['user_name']
        user_password = request.POST['user_password']
        user_email = request.POST['user_email']
        newUser = User(user_name=user_name,
                        user_password=user_password, 
                        user_email=user_email
                        )
        newUser.save()
        
        users = User.objects.all()
        quickResponse = []
        for user in users:
            quickResponse.append(user.user_name+" - "+user.user_password+" - "+user.user_email)
        return HttpResponse("/n".join(quickResponse))
    return HttpResponse("didn't get new user info from form")

def newEvent(request):
    form = EventForm()
    return render(request, 'newEvent.html', {'form':form})

def eventCreated(request):
    if request.POST:
#        desc = request.POST['event_description']
#
#        newEvent = Event(event_description=desc)
#        newEvent.save()
#
#        events = Event.objects.all()
#        descList = [event.event_description for event in events]
#        lastDesc = descList[-1]
#        return HttpResponse(lastDesc)
        return HttpResonse('got new event info from form')
    else: return HttpResponse("didn't get new event info from form")
