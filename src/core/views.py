from rest_framework.generics import ListAPIView
from core.models import Event
from core.serializers import ListEventSerializer


class ListEventAPI(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = ListEventSerializer