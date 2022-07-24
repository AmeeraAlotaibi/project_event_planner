from django.shortcuts import render
from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView, RetrieveAPIView
from .models import Event
from .serializers import EventsListSerializer

# Create your views here.
class EventsListView(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventsListSerializer