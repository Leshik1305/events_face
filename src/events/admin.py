# Register your models here.
from django.contrib import admin

from .models import Event, Place


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_filter = ["name"]
    search_fields = ["name"]
    ordering = ["name"]


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "date", "status"]
    list_filter = ["name", "date", "status", "place"]
    search_fields = ["name"]
    raw_id_fields = ["place"]
    date_hierarchy = "date"
    ordering = ["status", "name", "date"]
