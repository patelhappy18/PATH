

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from car_ride.models import Mycar
from django import forms
from PIL import Image


class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Parcel(models.Model):
    REQUEST_STATUS_CHOICES = (
        ('Requested', 'Requested'),
        ('Accepted', 'Accepted'),
        ('Declined', 'Declined'),
    )
    sender = models.CharField(max_length=150)
    recipient = models.CharField(max_length=150)
    source_city = models.TextField(null=True, blank=True)
    destination_city = models.TextField(null=True, blank=True)
    description = models.TextField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    is_delivered = models.BooleanField(default=False)
    image = models.ImageField(upload_to='parcel_service', default="", null=True, blank=True)
    requester = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requests_sent', null=True)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requests_received', null=True)
    is_accepted = models.CharField(max_length=50, choices=REQUEST_STATUS_CHOICES, default="Requested")
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    ride_id = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return f"Parcel from {self.source_city} to {self.destination_city} -"

class createParcelRide(models.Model):
    username = models.CharField(max_length=150)
    source = models.TextField()
    destination = models.TextField()
    description = models.TextField()
class ParcelService(models.Model):
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return f"Parcel from {self.source} to {self.destination}"

# class UserActivity(models.Model):
#     user = models.CharField(max_length=255)
#     activity = models.CharField(max_length=255)
#     timestamp = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f'{self.user.username} - {self.activity}'

class UserActivity(models.Model):
    reqstr = models.CharField(max_length=255, null=True, blank=True)
    recvr = models.CharField(max_length=255, null=True, blank=True)
    REQUEST_STATUS_CHOICES = (
        ('Requested', 'Requested'),
        ('Accepted', 'Accepted'),
        ('Declined', 'Declined'),
    )
    type = models.CharField(max_length=50, choices=REQUEST_STATUS_CHOICES, default="Requested")
    msg = models.CharField(max_length=255, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.reqstr} - {self.msg}'