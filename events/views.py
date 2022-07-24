from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Event
from .serializers import EventsListSerializer, EventDetailsSerializer, CreateEventSerializer
from rest_framework import filters
# Create your views here.
class EventsListView(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventsListSerializer


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
    