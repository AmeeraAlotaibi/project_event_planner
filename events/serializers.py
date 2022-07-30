from rest_framework import serializers
from .models import Event
from rest_framework.serializers import DateField, ValidationError
from datetime import timedelta, date

# List
class EventsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        exclude = ["image"]

# Details
class EventDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"
    
    
# Create
class CreateEventSerializer(serializers.ModelSerializer):
 
    start_date = DateField()
    end_date = DateField()

    class Meta:
        model = Event
        exclude = ["id"]

    def validate(self, data):
        if data["num_of_seats"] < data["booked_seats"]:
            raise ValidationError("Cannot book anymore. This event is fully booked!")
        
        if data["start_date"] > data["end_date"]:
            raise ValidationError("Cannot start date after end date!")
        
        if data["start_date"] < (date.today() + timedelta(days=1)):
            raise ValidationError("You can't book event in the past! (...unless you're Doctor Who ;) )")

        return data


