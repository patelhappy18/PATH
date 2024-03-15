# Generated by Django 5.0.3 on 2024-03-14 19:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "car_ride",
            "0002_remove_bookedride_driver_remove_bookedride_passenger_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="ContactUs",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=80)),
                ("email", models.EmailField(max_length=80, unique=True)),
                ("phone", models.CharField(blank=True, max_length=11)),
                ("msg", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Mycar",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("car_num", models.CharField(max_length=10, unique=True)),
                ("company", models.CharField(max_length=30)),
                ("car_name", models.CharField(max_length=30)),
                ("car_type", models.CharField(max_length=30)),
                ("from_place", models.CharField(max_length=30)),
                ("to_place", models.CharField(max_length=30)),
                ("from_date", models.DateField(null=True)),
                ("to_date", models.DateField(null=True)),
                ("price", models.FloatField()),
                (
                    "car_img",
                    models.ImageField(
                        blank=True, default="", null=True, upload_to="cars"
                    ),
                ),
                ("total_seats", models.IntegerField()),
                ("seats_booked", models.IntegerField(default=0)),
                (
                    "cust",
                    models.ForeignKey(
                        blank=True,
                        max_length=100,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="car_ride.customer",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Booking",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("contact", models.CharField(max_length=11)),
                ("email", models.EmailField(max_length=80)),
                ("pickup", models.DateField()),
                ("dropoff", models.DateField()),
                ("pick_add", models.CharField(max_length=100)),
                ("drop_add", models.CharField(max_length=100)),
                ("date_added", models.DateTimeField(auto_now_add=True)),
                ("num_seats_booked", models.IntegerField(default=0)),
                (
                    "name",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="car_ride.customer",
                    ),
                ),
                (
                    "car",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="car_ride.mycar",
                    ),
                ),
            ],
        ),
    ]