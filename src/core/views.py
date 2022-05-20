from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveDestroyAPIView
from core.models import Category, Country, City, Ground, Currency, Event, Order, Basket
from core.serializers import CategorySerializer, CountrySerializer, CitySerializer, GroundSerializer, GroundCreateSerializer, CurrencySerializer, EventSerializer, EventCreateSerializer, OrderSerializer, OrderCreateSerializer, BasketSerializer, BasketCreateSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from core.permissions import IsOwner


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
    permission_classes = (IsAdminUser, )


class UpdateCategoryAPI(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "id"
    permission_classes = (IsAdminUser, )


class DestroyCategoryAPI(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "id"
    permission_classes = (IsAdminUser, )





class CreateCountryAPI(CreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    lookup_field = "id"
    permission_classes = (IsAdminUser, )


class DestroyCountryAPI(DestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    lookup_field = "id"
    permission_classes = (IsAdminUser, )





class CreateCityAPI(CreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    lookup_field = "id"
    permission_classes = (IsAdminUser, )


class DestroyCityAPI(DestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    lookup_field = "id"
    permission_classes = (IsAdminUser, )





class CreateGroundAPI(CreateAPIView):
    queryset = Ground.objects.all()
    serializer_class = GroundCreateSerializer
    lookup_field = "id"
    permission_classes = (IsAdminUser, )


class RetrieveDestroyGroundAPI(RetrieveDestroyAPIView):
    queryset = Ground.objects.all()
    serializer_class = GroundSerializer
    lookup_field = "id"
    permission_classes = (IsAdminUser, )





class CreateCurrencyAPI(CreateAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    lookup_field = "id"
    permission_classes = (IsAdminUser, )


class DestroyCurrencyAPI(DestroyAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    lookup_field = "id"
    permission_classes = (IsAdminUser, )





class ListEventAPI(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class RetrieveEventAPI(RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    lookup_field = "id"


class CreateEventAPI(CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventCreateSerializer
    permission_classes = (IsAdminUser, )


class UpdateEventAPI(UpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    lookup_field = "id"
    permission_classes = (IsAdminUser, )


class DestroyEventAPI(DestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    lookup_field = "id"
    permission_classes = (IsAdminUser, )





class ListOrderAPI(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAdminUser, )


class RetrieveOrderAPI(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = "id"
    permission_classes = (IsOwner|IsAdminUser, ) 


class CreateOrderAPI(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
    permission_classes = (IsAuthenticated, )


class DestroyOrderAPI(DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = "id"
    permission_classes = (IsAdminUser, )





class RetrieveBasketAPI(RetrieveAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    lookup_field = "id"
    permission_classes = (IsAdminUser, )


class CreateBasketAPI(CreateAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketCreateSerializer
    permission_classes = (IsAuthenticated, )
