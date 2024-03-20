# Generated by Django 5.0.3 on 2024-03-18 17:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Car",
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
                ("make", models.CharField(max_length=100)),
                ("model", models.CharField(max_length=100)),
                ("year", models.PositiveIntegerField()),
                ("daily_rate", models.DecimalField(decimal_places=2, max_digits=8)),
                ("available", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="CustomUser",
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
                ("email", models.EmailField(max_length=254, unique=True)),
                ("first_name", models.CharField(max_length=30)),
                ("last_name", models.CharField(max_length=30)),
                ("date_of_birth", models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="RentalReservation",
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
                ("rental_start_date", models.DateField()),
                ("rental_end_date", models.DateField()),
                ("total_cost", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("reserved", "Reserved"),
                            ("canceled", "Canceled"),
                            ("completed", "Completed"),
                        ],
                        default="reserved",
                        max_length=20,
                    ),
                ),
                (
                    "car",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="car_rental.car"
                    ),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="car_rental.customuser",
                    ),
                ),
            ],
        ),
    ]
