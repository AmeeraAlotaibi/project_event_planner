from datetime import date
from xml.dom import ValidationErr
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.forms import ValidationError
# Create your models here.
class Event(models.Model):
    organizer = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=25)
    email = models.EmailField()
    image = models.CharField(max_length=300)
    num_of_seats = models.PositiveIntegerField(validators=[MinValueValidator(5)])
    booked_seats = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(num_of_seats)])
    start_date = models.DateField()
    end_date = models.DateField()
    
    # def validate_start_date(start_date):
    #     if start_date < date.today():
    #         raise ValidationError("Date Cannot be in the past")

    def __str__(self):
        return self.name