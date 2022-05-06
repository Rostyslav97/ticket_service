from django.urls import path
from core.views import ListEventAPI, RetrieveEventAPI, CreateEventAPI, DestroyEventAPI


urlpatterns = [
    path('events/', ListEventAPI.as_view()),
    path('events/<int:id>/', RetrieveEventAPI.as_view()),
    path('events/create/', CreateEventAPI.as_view()),
    path('events/destroy/<int:id>/', DestroyEventAPI.as_view())
]