from __future__ import unicode_literals
from django.db import models


class Room(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=255)
    description = models.TextField()
    exits = models.ManyToManyField("Exit", blank=True, null=True)


class Exit(models.Model):
    def __str__(self):
        if self.to_room:
            name = self.to_room.name
        else:
            name = None

        return self.name + " to " + (name or " Nowhere")

    name = models.CharField(max_length=255)
    to_room = models.OneToOneField(Room, blank=True, null=True)
