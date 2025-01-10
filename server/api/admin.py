from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'points', 'timestamp', 'reason')  # Replace 'location' with 'reason'
