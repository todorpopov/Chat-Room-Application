from django.contrib.auth.models import User
from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    users_online = models.IntegerField()

class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    date = models.TextField()
    date_to_sort_by = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('date_to_sort_by',)
