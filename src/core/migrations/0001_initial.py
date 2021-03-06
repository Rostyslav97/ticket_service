# Generated by Django 4.0.4 on 2022-05-20 08:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=50, unique=True, verbose_name="Category")),
                ("description", models.TextField(blank=True, null=True, verbose_name="Description")),
            ],
        ),
        migrations.CreateModel(
            name="City",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=70, verbose_name="City")),
            ],
        ),
        migrations.CreateModel(
            name="Country",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=50, unique=True, verbose_name="Country")),
            ],
        ),
        migrations.CreateModel(
            name="Currency",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=50, verbose_name="Currency")),
            ],
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "customer",
                    models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Ground",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100, unique=True, verbose_name="Ground")),
                ("adress", models.CharField(max_length=100, verbose_name="Adress")),
                ("capacity", models.PositiveIntegerField(verbose_name="Capacity")),
                ("city", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="core.city")),
            ],
        ),
        migrations.CreateModel(
            name="Event",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100, verbose_name="Name")),
                ("poster", models.ImageField(blank=True, null=True, upload_to="", verbose_name="Poster")),
                ("price", models.PositiveIntegerField(verbose_name="Price")),
                ("date_time", models.DateTimeField()),
                ("category", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="core.category")),
                ("currency", models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to="core.currency")),
                ("ground", models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to="core.ground")),
            ],
        ),
        migrations.AddField(
            model_name="city",
            name="country",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="core.country"),
        ),
        migrations.CreateModel(
            name="Basket",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("amount", models.IntegerField()),
                ("order_date_time", models.DateTimeField(auto_now_add=True)),
                ("event", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="core.event")),
                ("order", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="core.order")),
            ],
        ),
    ]
