from rest_framework import serializers

from .models import EventOrganiser, Event, Tag, Category


# Serialize Event Organizer
class EventOrganiserSerializer(serializers.ModelSerializer):

  class Meta:
    model = EventOrganiser
    fields = '__all__'


# Serialize tag
class TagSerializer(serializers.ModelSerializer):

  class Meta:
    model = Tag
    fields = '__all__'
  

# Serialize Category
class CategorySerializer(serializers.ModelSerializer):

  class Meta:
    model = Category
    fields = '__all__'

# Serialize event
class EventSerializer(serializers.ModelSerializer):

  class Meta:
    model = Event
    fields = '__all__'