"""Doscting."""
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Doscting."""

    class Meta:
        """Doscting."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
