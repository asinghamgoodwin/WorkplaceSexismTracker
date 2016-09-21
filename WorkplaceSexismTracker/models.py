from django.db import models
import datetime
#import django.utils.timezone as timezone

class Category(models.Model):
    category_name = models.CharField(max_length=100)


class User(models.Model):
    user_name = models.CharField(max_length=100)
    user_password = models.CharField(max_length=100)
    user_email = models.EmailField()


class Event(models.Model):
    event_user = models.ForeignKey(User, on_delete=models.CASCADE)
    #if the user is deleted, delete this event too
    event_date = models.DateField(default=datetime.date.today)
    event_people = models.CharField(max_length=100, null=True, blank=True)
    event_private_yesno = models.NullBooleanField(null=True, blank=True)
    event_description = models.CharField(max_length=500, null=True, blank=True)
    event_immediate_response_yesno = models.NullBooleanField(null=True, blank=True)
    event_reaction = models.CharField(max_length=500, null=True, blank=True)
    event_category = models.CharField(max_length=100, null=True, blank=True,
                                                choices=[(1,"exclusion"),
                                                        (2,"harassment"),
                                                        (3,"stereotyping")
                                                        ])
    event_cost_rating = models.IntegerField(choices=[(1,1),(2,2),(3,3),(4,4),(5,5)],
                                            null=True, blank=True)
    event_cost_desc = models.CharField(max_length=100, null=True, blank=True)


#    uncomment this out later! once we learn how to have initial data in the database
#    event_category = models.ForeignKey(Category, on_delete=models.SET_NULL)
    #if the category is deleted, make ths event's category 'null'

