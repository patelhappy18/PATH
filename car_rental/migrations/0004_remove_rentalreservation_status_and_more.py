# Generated by Django 5.0.3 on 2024-03-14 17:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("car_rental", "0003_delete_photo_car_color_car_photo"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="rentalreservation",
            name="status",
        ),
        migrations.AddField(
            model_name="rentalreservation",
            name="car_type",
            field=models.CharField(
                choices=[
                    ("sedan", "Sedan"),
                    ("suv", "SUV"),
                    ("truck", "Truck"),
                    ("van", "Van"),
                ],
                default="sedan",
                max_length=20,
            ),
        ),
        migrations.AddField(
            model_name="rentalreservation",
            name="pickup_location",
            field=models.CharField(
                choices=[
                    ("London", "London"),
                    ("Windsor", "Windsor"),
                    ("Toronto", "Toronto"),
                    ("Hamilton", "Hamilton"),
                ],
                default="Windsor",
                max_length=100,
            ),
        ),
        migrations.AddField(
            model_name="rentalreservation",
            name="pickup_time",
            field=models.DateTimeField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="rentalreservation",
            name="return_time",
            field=models.DateTimeField(default=1),
            preserve_default=False,
        ),
    ]
