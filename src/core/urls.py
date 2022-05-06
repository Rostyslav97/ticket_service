from django.urls import path
from core.views import ListEventAPI, RetrieveEventAPI, CreateEventAPI, DestroyEventAPI, ListCartAPI, RetrieveCartAPI, CreateCartAPI, DestroyCartAPI


urlpatterns = [
    path('events/', ListEventAPI.as_view()),
    path('events/<int:id>/', RetrieveEventAPI.as_view()),
    path('events/create/', CreateEventAPI.as_view()),
    path('events/destroy/<int:id>/', DestroyEventAPI.as_view()),
    path('cart/', ListCartAPI.as_view()),
    path('cart/<int:id>/', RetrieveCartAPI.as_view()),
    path('cart/create/', CreateCartAPI.as_view()),
    path('cart/destroy/<int:id>/', DestroyCartAPI.as_view()),
]