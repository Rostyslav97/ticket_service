from django.db import models
from django.conf import settings


class Category(models.Model):
    name = models.CharField("Category", max_length=50)
    description = models.TextField("Description")

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField("City", max_length=70)

    def __str__(self):
        return self.name


class Ground(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField("Ground", max_length=100)
    adress = models.CharField("Adress", max_length=100)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField("Name", max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    poster = models.ImageField("Poster")
    ground = models.ForeignKey(Ground, on_delete=models.DO_NOTHING)
    price = models.PositiveIntegerField("Price", help_text="put amount in hrn")
    date_time = models.DateTimeField()

    def __str__(self):
        return self.name


class Cart(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=False, on_delete=models.SET_NULL)
    event = models.ManyToManyField(Event)
    amount = models.IntegerField()
    order_date_time = models.DateTimeField(auto_now_add=True)