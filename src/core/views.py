from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView
from core.models import Event
from core.serializers import ListRetrieveDestroyEventSerializer, CreateEventSerializer


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