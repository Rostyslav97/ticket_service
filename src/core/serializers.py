from rest_framework import serializers
from core.models import Category, Country, City, Ground, Currency, Event, Cart
from django.contrib.auth import get_user_model


User = get_user_model()


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"





class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"





class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"





class GroundSerializer(serializers.ModelSerializer):
    city = serializers.SlugRelatedField(slug_field="name", read_only=True)
    class Meta:
        model = Ground
        fields = "__all__"


class GroundCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ground
        fields = "__all__"





class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = "__all__"





class EventSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field="name", read_only=True)
    ground = GroundSerializer(read_only=True)
    currency = serializers.SlugRelatedField(slug_field="name", read_only=True)
    class Meta:
        model = Event
        fields = "__all__"


class EventCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"




class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = (
            "password",
            "last_login",
            "is_superuser",
            "is_staff",
            "is_active",
            "groups",
            "user_permissions",
            "date_joined"
        )





class CartSerializer(serializers.ModelSerializer):
    event = EventSerializer(read_only=True, many=True)
    customer = CustomerSerializer(read_only=True)
    class Meta:
        model = Cart
        fields = "__all__"



class CartCreateSerializer(serializers.ModelSerializer):
    customer = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Cart
        fields = "__all__"
