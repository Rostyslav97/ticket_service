from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from core.models import Category, Country, City, Event, Cart
from core.serializers import EventSerializer, CountrySerializer, CitySerializer, CreateEventSerializer, CartSerializer, CreateCartSerializer, CategorySerializer


class ListCategoryAPI(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class RetrieveCategoryAPI(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "id"


class CreateCategoryAPI(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UpdateCategoryAPI(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "id"


class DestroyCategoryAPI(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "id"





class CreateCountryAPI(CreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    lookup_field = "id"


class DestroyCountryAPI(DestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    lookup_field = "id"





class CreateCityAPI(CreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    lookup_field = "id"


class DestroyCityAPI(DestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    lookup_field = "id"





class ListEventAPI(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class RetrieveEventAPI(RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    lookup_field = "id"


class CreateEventAPI(CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = CreateEventSerializer


class UpdateEventAPI(UpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    lookup_field = "id"


class DestroyEventAPI(DestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    lookup_field = "id"





class ListCartAPI(ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class RetrieveCartAPI(RetrieveAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    lookup_field = "id"


class CreateCartAPI(CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CreateCartSerializer


class DestroyCartAPI(DestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    lookup_field = "id"
