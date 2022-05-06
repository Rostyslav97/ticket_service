from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from core.models import Event
from core.serializers import ListRetrieveEventSerializer, CreateEventSerializer


class ListEventAPI(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = ListRetrieveEventSerializer


class RetrieveEventAPI(RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = ListRetrieveEventSerializer
    lookup_field = "id"


class CreateEventAPI(CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = CreateEventSerializer