from django.db import models
from django.conf import settings


class Category(models.Model):
    name = models.CharField("Category", max_length=50, unique=True)
    description = models.TextField("Description", null=True, blank=True)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField("Country", max_length=50, unique=True)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField("City", max_length=70)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Ground(models.Model):
    name = models.CharField("Ground", max_length=100, unique=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    adress = models.CharField("Adress", max_length=100)
    capacity = models.PositiveIntegerField("Capacity")

    def __str__(self):
        return self.name


class Currency(models.Model):
    name = models.CharField("Currency", max_length=50)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField("Name", max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    poster = models.ImageField("Poster", null=True, blank=True)
    ground = models.ForeignKey(Ground, on_delete=models.DO_NOTHING)
    currency = models.ForeignKey(Currency, on_delete=models.DO_NOTHING)
    price = models.PositiveIntegerField("Price")
    date_time = models.DateTimeField()

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.customer


class Basket(models.Model):
    event = models.ForeignKey("Event", on_delete=models.CASCADE)
    order = models.ForeignKey("Order", on_delete=models.CASCADE)
    amount = models.IntegerField(null=False, blank=False)
    order_date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.event