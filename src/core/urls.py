from django.urls import path
from core.views import ListEventAPI


urlpatterns = [
    path('events/', ListEventAPI.as_view()),
]