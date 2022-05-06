from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView
from core.models import Event, Cart
from core.serializers import EventSerializer, CreateEventSerializer, CartSerializer, CreateCartSerializer


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