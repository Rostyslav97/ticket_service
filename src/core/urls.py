from django.urls import path
from core.views import (
    ListCategoryAPI,
    RetrieveCategoryAPI,
    CreateCategoryAPI,
    UpdateCategoryAPI,
    DestroyCategoryAPI,
    CreateCountryAPI,
    DestroyCountryAPI,
    CreateCityAPI,
    DestroyCityAPI,
    CreateGroundAPI,
    RetrieveDestroyGroundAPI,
    CreateCurrencyAPI,
    DestroyCurrencyAPI,
    ListEventAPI,
    RetrieveEventAPI,
    CreateEventAPI,
    UpdateEventAPI,
    DestroyEventAPI,
    ListOrderAPI,
    RetrieveOrderAPI,
    CreateOrderAPI,
    DestroyOrderAPI,
    RetrieveBasketAPI,
    CreateBasketAPI,
)


app_name = "core"


urlpatterns = [
    path("categories/", ListCategoryAPI.as_view(), name="list_categories"),
    path("categories/<int:id>/", RetrieveCategoryAPI.as_view(), name="retrieve_categories"),
    path("categories/create/", CreateCategoryAPI.as_view(), name="create_categories"),
    path("categories/update/<int:id>/", UpdateCategoryAPI.as_view(), name="update_categories"),
    path("categories/destroy/<int:id>/", DestroyCategoryAPI.as_view(), name="destroy_categories"),
    path("countries/create/", CreateCountryAPI.as_view(), name="create_countries"),
    path("countries/destroy/<int:id>/", DestroyCountryAPI.as_view(), name="destroy_countries"),
    path("cities/create/", CreateCityAPI.as_view(), name="create_cities"),
    path("cities/destroy/<int:id>/", DestroyCityAPI.as_view(), name="destroy_cities"),
    path("grounds/create/", CreateGroundAPI.as_view(), name="create_grounds"),
    path("grounds/<int:id>/", RetrieveDestroyGroundAPI.as_view(), name="retrieve_grounds"),
    path("currencies/create/", CreateCurrencyAPI.as_view(), name="create_currencies"),
    path("currencies/destroy/<int:id>/", DestroyCurrencyAPI.as_view(), name="destroy_currencies"),
    path("events/", ListEventAPI.as_view(), name="list_events"),
    path("events/<int:id>/", RetrieveEventAPI.as_view(), name="retrieve_events"),
    path("events/create/", CreateEventAPI.as_view(), name="create_events"),
    path("events/update/<int:id>/", UpdateEventAPI.as_view(), name="update_events"),
    path("events/destroy/<int:id>/", DestroyEventAPI.as_view(), name="destroy_events"),
    path("orders/", ListOrderAPI.as_view(), name="list_orders"),
    path("orders/<int:id>/", RetrieveOrderAPI.as_view(), name="retrieve_orders"),
    path("orders/create/", CreateOrderAPI.as_view(), name="create_orders"),
    path("orders/destroy/<int:id>/", DestroyOrderAPI.as_view(), name="destroy_orders"),
    path("baskets/<int:id>/", RetrieveBasketAPI.as_view(), name="retrieve_baskets"),
    path("baskets/create/", CreateBasketAPI.as_view(), name="create_baskets"),
]
