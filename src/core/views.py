from rest_framework.generics import ListAPIView, RetrieveAPIView
from core.models import Event
from core.serializers import EventSerializer


class ListEventAPI(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class RetrieveEventAPI(RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    lookup_field = "id"