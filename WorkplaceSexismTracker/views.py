from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from models import Event, User, Category
from forms import EventForm, UserForm, LoginForm

## THIS SECTION IS JUST BARE-BONES, LOTS TO IMPROVE UPON/IMPLEMENT
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
        return HttpResponse(" | ".join(quickResponse))
    return HttpResponse("didn't get new user info from form")
## END OF BORING PARTS


#record a new event that took place
def newEvent(request, user_id):
    try:
        userFromId = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise Http404("That user does not exist")

    form = EventForm()
    return render(request, 'newEvent.html', {'form':form, 'user_id':user_id})

#save a new event into the database
#this gets called when someone submits a form on the newEvent page
def eventCreated(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise Http404("That user does not exist")

    if request.POST:
        event_user = user
        event_date = request.POST['event_date']
        event_people = request.POST['event_people']
        event_private_yesno  = request.POST['event_private_yesno']
        event_description = request.POST['event_description']
        event_immediate_response_yesno = request.POST['event_immediate_response_yesno']
        event_reaction = request.POST['event_reaction']
        event_category = request.POST['event_category']
        event_cost_rating = request.POST['event_cost_rating']
        event_cost_desc = request.POST['event_cost_desc']

        newEvent = Event(event_user=event_user,
                        event_date=event_date,
                        event_people=event_people,
                        event_private_yesno=event_private_yesno,
                        event_description=event_description,
                        event_immediate_response_yesno=event_immediate_response_yesno,
                        event_reaction=event_reaction,
                        event_category=event_category,
                        event_cost_rating=event_cost_rating,
                        event_cost_desc=event_cost_desc,
                        )

        newEvent.save()
        return HttpResponseRedirect(reverse('home', args=(user_id)))
    else: return HttpResponse("didn't get new event info from form")


def home(request, user_id):
    try:
        userFromId = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise Http404("That user does not exist")

    allEvents = Event.objects.all()
    userEvents = [e for e in allEvents if e.event_user == userFromId]
    eventsByDate = userEvents #later, sort this.
    return render(request, 'home.html', {'user_id':user_id, 'events':eventsByDate})

def info(request):
    return HttpResponse("here we'd like to have lots of info about recognizing and responding to sexism in the workplace")




