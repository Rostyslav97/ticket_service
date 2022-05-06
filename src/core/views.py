from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView
from core.models import Event, Cart
from core.serializers import ListRetrieveDestroyEventSerializer, CreateEventSerializer, CreateCartSerializer


class ListEventAPI(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = ListRetrieveDestroyEventSerializer


class RetrieveEventAPI(RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = ListRetrieveDestroyEventSerializer
    lookup_field = "id"


class CreateEventAPI(CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = CreateEventSerializer


class DestroyEventAPI(DestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = ListRetrieveDestroyEventSerializer
    lookup_field = "id"



class CartCreateAPI(CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CreateCartSerializer