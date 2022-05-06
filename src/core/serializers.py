from rest_framework import serializers
from core.models import Event


class EventSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field="name", read_only=True)
    ground = serializers.SlugRelatedField(slug_field="name", read_only=True)
    currency = serializers.SlugRelatedField(slug_field="name", read_only=True)
    class Meta:
        model = Event
        exclude = ("id", )