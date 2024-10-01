"""Doscting."""
from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    """Doscting."""

    list_display = ('title', 'description', 'completed')


admin.site.register(Task, TaskAdmin)
