from django.db import models

class Event(models.Model):
    event_description = models.CharField(max_length=500)

