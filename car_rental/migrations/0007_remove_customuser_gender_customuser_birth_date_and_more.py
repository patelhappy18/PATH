# Generated by Django 5.0.3 on 2024-03-17 16:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("car_rental", "0006_remove_customuser_date_of_birth_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="gender",
        ),
        migrations.AddField(
            model_name="customuser",
            name="birth_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="customuser",
            name="country",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AddField(
            model_name="customuser",
            name="dl_number",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AddField(
            model_name="customuser",
            name="expiry_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="customuser",
            name="issueing_country",
            field=models.CharField(
                choices=[("Canada", "Canada"), ("USA", "USA")],
                default="Windsor",
                max_length=100,
            ),
        ),
        migrations.AddField(
            model_name="customuser",
            name="lname",
            field=models.CharField(blank=True, default="", max_length=80),
        ),
        migrations.AddField(
            model_name="customuser",
            name="postal_code",
            field=models.CharField(default="", max_length=100),
        ),
    ]