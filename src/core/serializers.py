from rest_framework import serializers
from core.models import Event, Cart


class ListRetrieveDestroyEventSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field="name", read_only=True)
    ground = serializers.SlugRelatedField(slug_field="name", read_only=True)
    currency = serializers.SlugRelatedField(slug_field="name", read_only=True)
    class Meta:
        model = Event
        exclude = ("id", )


class CreateEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        exclude = ("id", )



class CreateCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        exclude = ("id", )