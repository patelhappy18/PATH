# Generated by Django 5.0.3 on 2024-03-19 04:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("parcel_service", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="createParcelRide",
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
                ("username", models.CharField(max_length=150)),
                ("source", models.TextField()),
                ("destination", models.TextField()),
                ("description", models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name="parcel",
            name="delivery_date",
        ),
        migrations.AlterField(
            model_name="parcel",
            name="destination",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="parcel",
            name="recipient",
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name="parcel",
            name="sender",
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name="parcel",
            name="source",
            field=models.TextField(),
        ),
    ]
