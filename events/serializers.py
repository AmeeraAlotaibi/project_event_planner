from rest_framework import serializers
from .models import Event

class EventsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        exclude = ["image"]