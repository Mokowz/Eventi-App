from django.contrib import admin

from .models import EventOrganiser, Event, Tag, Category

# Register your models here.
admin.site.register(Event)
admin.site.register(EventOrganiser)
admin.site.register(Tag)
admin.site.register(Category)
