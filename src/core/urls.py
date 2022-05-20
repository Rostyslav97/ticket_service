from django.urls import path
from core.views import ListCategoryAPI, RetrieveCategoryAPI, CreateCategoryAPI, UpdateCategoryAPI, DestroyCategoryAPI, CreateCountryAPI, DestroyCountryAPI, CreateCityAPI, DestroyCityAPI, CreateGroundAPI, RetrieveDestroyGroundAPI, CreateCurrencyAPI, DestroyCurrencyAPI, ListEventAPI, RetrieveEventAPI, CreateEventAPI, UpdateEventAPI, DestroyEventAPI, ListOrderAPI, RetrieveOrderAPI, CreateOrderAPI, DestroyOrderAPI, RetrieveBasketAPI, CreateBasketAPI


urlpatterns = [
    path('category/', ListCategoryAPI.as_view()),
    path('category/<int:id>/', RetrieveCategoryAPI.as_view()),
    path('category/create/', CreateCategoryAPI.as_view()),
    path('category/update/<int:id>/', UpdateCategoryAPI.as_view()),
    path('category/destroy/<int:id>/', DestroyCategoryAPI.as_view()),

    path('country/create/', CreateCountryAPI.as_view()),
    path('country/destroy/<int:id>/', DestroyCountryAPI.as_view()),

    path('city/create/', CreateCityAPI.as_view()),
    path('city/destroy/<int:id>/', DestroyCityAPI.as_view()),

    path('ground/create/', CreateGroundAPI.as_view()),
    path('ground/<int:id>/', RetrieveDestroyGroundAPI.as_view()),

    path('currency/create/', CreateCurrencyAPI.as_view()),
    path('currency/destroy/<int:id>/', DestroyCurrencyAPI.as_view()),


    path('events/', ListEventAPI.as_view()),
    path('events/<int:id>/', RetrieveEventAPI.as_view()),
    path('events/create/', CreateEventAPI.as_view()),
    path('events/update/<int:id>/', UpdateEventAPI.as_view()),
    path('events/destroy/<int:id>/', DestroyEventAPI.as_view()),
    
    path('order/', ListOrderAPI.as_view()),
    path('order/<int:id>/', RetrieveOrderAPI.as_view()),
    path('order/create/', CreateOrderAPI.as_view()),
    path('order/destroy/<int:id>/', DestroyOrderAPI.as_view()),

    path('basket/<int:id>/', RetrieveBasketAPI.as_view()),
    path('basket/create/', CreateBasketAPI.as_view())
]
