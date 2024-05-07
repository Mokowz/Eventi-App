from django.urls import path
from .views import (
  EventListView,
  EventRetrieveView,
  EventOrganiserListView,
  EventOrganiserRetrieveView,
  TagListView,
  TagRetrieveView,
  CategoryListView,
  CategoryRetrieveView,
)

urlpatterns = [
    path('events/', EventListView.as_view(), name="events-list"),
    path('events/<int:pk>/', EventRetrieveView.as_view(), name="event-instance"),

    path('organisers/', EventOrganiserListView.as_view(), name="organisers-list"),
    path('organisers/<int:pk>/', EventOrganiserRetrieveView.as_view(), name="organiser-instance"),

    path('tags/', TagListView.as_view(), name="tags-list"),
    path('tags/<int:pk>/', TagRetrieveView.as_view(), name="tag-instance"),

    path('categories/', CategoryListView.as_view(), name="category-list"),
    path('categories/<int:pk>/', CategoryRetrieveView.as_view(), name="category-instance"),
]