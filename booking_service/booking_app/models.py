from django.db import models

class Room(models.Model):
    describe = models.TextField(max_length=1000)
    price = models.FloatField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.describe

class Reservation(models.Model):
    room = models.ForeignKey('Room', on_delete=models.CASCADE)
    booking_starts = models.DateField()
    booking_ends = models.DateField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
