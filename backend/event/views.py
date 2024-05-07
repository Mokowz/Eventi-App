from django.shortcuts import render
from rest_framework import generics

from .models import EventOrganiser, Event, Tag, Category
from .serializers import EventOrganiserSerializer, EventSerializer, TagSerializer, CategorySerializer

# GET and POST the list of events
class EventListView(generics.ListCreateAPIView):
  queryset = Event.objects.all()
  serializer_class = EventSerializer

# Retrieve a specific event
class EventRetrieveView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Event.objects.all()
  serializer_class = EventSerializer


# Event Organiser
# GET and POST the list of Event organisers
class EventOrganiserListView(generics.ListCreateAPIView):
  queryset = EventOrganiser.objects.all()
  serializer_class = EventOrganiserSerializer

# Retrieve a specific Event organiser
class EventOrganiserRetrieveView(generics.RetrieveUpdateDestroyAPIView):
  queryset = EventOrganiser.objects.all()
  serializer_class = EventOrganiserSerializer


# Tag
# GET and POST the list of Tags
class TagListView(generics.ListCreateAPIView):
  queryset = Tag.objects.all()
  serializer_class = TagSerializer

# Retrieve a specific Tags
class TagRetrieveView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Tag.objects.all()
  serializer_class = TagSerializer

# Category
# GET and POST the list of Categorys
class CategoryListView(generics.ListCreateAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer

# Retrieve a specific Category
class CategoryRetrieveView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer
