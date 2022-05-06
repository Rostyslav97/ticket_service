from rest_framework import serializers
from core.models import Event


class ListEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        exclude = ("id", )