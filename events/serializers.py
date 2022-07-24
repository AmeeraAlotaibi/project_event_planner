from rest_framework import serializers
from .models import Event

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
    class Meta:
        model = Event
        exclude = ["id"]