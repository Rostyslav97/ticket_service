from rest_framework import serializers
from core.models import Category, Country, City, Ground, Currency, Event, Cart


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ("id", )





class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        exclude = ("id", )





class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        exclude = ("id", )





class GroundSerializer(serializers.ModelSerializer):
    city = serializers.SlugRelatedField(slug_field="name", read_only=True)
    class Meta:
        model = Ground
        exclude = ("id", )


class GroundCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ground
        exclude = ("id", )





class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        exclude = ("id", )





class EventSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field="name", read_only=True)
    ground = GroundSerializer(read_only=True)
    currency = serializers.SlugRelatedField(slug_field="name", read_only=True)
    class Meta:
        model = Event
        exclude = ("id", )


class EventCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        exclude = ("id", )





class CartSerializer(serializers.ModelSerializer):
    event = EventSerializer(read_only=True, many=True)
    class Meta:
        model = Cart
        exclude = ("id", )


class CartCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        exclude = ("id", )
