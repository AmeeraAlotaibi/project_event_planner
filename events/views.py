from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Event
from .serializers import EventsListSerializer, EventDetailsSerializer, CreateEventSerializer
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from django.db.models import F



# Create your views here.
class EventsListView(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventsListSerializer
    pagination_class = PageNumberPagination


class EventDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventDetailsSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'event_id'


class AddEventView(CreateAPIView):
    serializer_class = CreateEventSerializer
    

class SearchEventView(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventsListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]


class FullyBookedView(ListAPIView):
    queryset = Event.objects.filter(booked_seats= F('num_of_seats'))
    serializer_class = EventsListSerializer



