

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Parcel(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_parcels')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_parcels')
    source = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='source_parcels')
    destination = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='destination_parcels')
    description = models.TextField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    is_delivered = models.BooleanField(default=False)
    delivery_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Parcel from {self.source} to {self.destination} - {self.description}"
