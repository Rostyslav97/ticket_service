from rest_framework import serializers
from core.models import Category, Country, Event, Cart


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ("id", )





class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        exclude = ("id", )





class EventSerializer(serializers.ModelSerializer):
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





class CartSerializer(serializers.ModelSerializer):
    event = EventSerializer(read_only=True, many=True)
    class Meta:
        model = Cart
        exclude = ("id", )


class CreateCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        exclude = ("id", )
