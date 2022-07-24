from django.db import models

# Create your models here.
class Event(models.Model):
    organizer = models.CharField(max_length=50)
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=100)
    image = models.CharField(max_length=300)
    num_of_seats = models.PositiveIntegerField()
    booked_seats = models.PositiveIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name