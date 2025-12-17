from django.contrib import admin

from .models import SyncResult


@admin.register(SyncResult)
class SyncResultAdmin(admin.ModelAdmin):
    list_display = ["id", "created_at", "new_events_count", "updated_events_count"]
    list_filter = ["created_at"]
    readonly_fields = ["created_at"]
    ordering = ["-created_at"]
