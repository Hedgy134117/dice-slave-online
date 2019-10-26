from django.db import models

# Create your models here.
class Room(models.Model):
    name = models.TextField()
    label = models.SlugField(unique=True)

class Messge(models.Model):
    room = models.ForeignKey(Room, realted_name='messages')
    handle = models.TextField()
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)