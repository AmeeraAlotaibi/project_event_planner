from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.forms import ValidationError


# this makes sure the event name does not include the word "event" in it.
def validate_name(value):
        if not "event" in value.lower():
            return value
        else:
            raise ValidationError("The name cannot contain the word 'event'")


# Create your models here.
class Event(models.Model):  
    
    organizer = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=25, validators=[validate_name])
    email = models.EmailField()
    image = models.CharField(max_length=300)
    num_of_seats = models.PositiveIntegerField(validators=[MinValueValidator(5)])
    booked_seats = models.PositiveIntegerField(default=0)
    start_date = models.DateField()
    end_date = models.DateField()
    


    def __str__(self):
        return self.name

