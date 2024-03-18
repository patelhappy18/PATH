from datetime import datetime

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

from car_ride.models import Customer


class CustomUser(models.Model):

    pp_issueing_country = [
        ('Canada', 'Canada'),
        ('USA', 'USA'),
    ]

    email = models.EmailField(max_length=80, unique=True,default='')
    password = models.CharField(max_length=128,null=False,default='')
    #
    # password = models.CharField(max_length=50,
    #                             required=True,
    #                             label=("Password"),
    #                             widget=models.PasswordInput(attrs={'placeholder': 'Password',
    #                                                               'class': 'form-control',
    #                                                               'data-toggle': 'password',
    #                                                               'id': 'password',
    #                                                               }))


    fullname =models.CharField(max_length=100, null=False,default='')
    country = models.CharField(max_length=100, blank=True, null=False,default='')
    address = models.CharField(max_length=100,blank=True, null=False, default='')
    city = models.CharField(max_length=100,blank=True, null=False,default='')
    state = models.CharField(max_length=100,blank=True, null=False,default='')
    postal_code = models.CharField(max_length=100,blank=True, null=False,default='')
    mobile = models.CharField(max_length=11,blank=True, null=False,default='')

    issueing_country = models.CharField(max_length=100,blank=True, choices=pp_issueing_country, default='Windsor')
    dl_number = models.CharField(max_length=100,blank=True, null=False,default='')
    expiry_date = models.DateTimeField(null=True, blank=True)
    birth_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.fullname} - {self.email}"


class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    daily_rate = models.DecimalField(max_digits=8, decimal_places=2)
    available = models.BooleanField(default=True)
    color = models.CharField(max_length=50,default="unknown")
    photo = models.ImageField(upload_to='car_photos/', null=True, blank=True)

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

# Rental Reservation Model
class RentalReservation(models.Model):
    STATUS_CHOICES = [
        ('reserved', 'Reserved'),
        ('canceled', 'Canceled'),
        ('completed', 'Completed'),
    ]

    car_type_choices = [
        ('sedan', 'Sedan'),
        ('suv', 'SUV'),
        ('truck', 'Truck'),
        ('van', 'Van'),
        # Add more choices as needed
    ]

    PICKUP_LOCATIONS = [
        ('London', 'London'),
        ('Windsor', 'Windsor'),
        ('Toronto', 'Toronto'),
        ('Hamilton', 'Hamilton'),
        # Add more locations as needed
    ]

    rental_start_date = models.DateField(default=timezone.now)
    rental_end_date = models.DateField(default=timezone.now)
    pickup_time = models.DateTimeField(default=timezone.now)
    return_time = models.DateTimeField(default=timezone.now)

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,default=None)  # Use Customer model here
    pickup_location = models.CharField(max_length=100, choices=PICKUP_LOCATIONS, default='Windsor')

    car_type = models.CharField(max_length=20, choices=car_type_choices,default="sedan")

    def __str__(self):
        return f"{self.car} - {self.customer} "


class RentalInvoice(models.Model):
    rental_reservation = models.OneToOneField('RentalReservation', on_delete=models.CASCADE)
    invoice_number = models.CharField(max_length=100, unique=True)
    issue_date = models.DateField()
    due_date = models.DateField()
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Invoice #{self.invoice_number} - Total: ${self.amount_due}"


class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.name


from django.db import models

class CustomerReview(models.Model):
    customer = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    car = models.ForeignKey('Car', on_delete=models.CASCADE)
    rating = models.IntegerField()
    review_text = models.TextField()
    date_posted = models.DateField()

    def __str__(self):
        return f"Review by {self.customer} for {self.car}"

class InsurancePolicy(models.Model):
    policy_number = models.CharField(max_length=100)
    provider_name = models.CharField(max_length=100)
    coverage_start_date = models.DateField()
    coverage_end_date = models.DateField()
    premium_amount = models.DecimalField(max_digits=10, decimal_places=2)
    deductible_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Policy #{self.policy_number} - Provider: {self.provider_name}"

class RentalTransaction(models.Model):
    rental_reservation = models.OneToOneField('RentalReservation', on_delete=models.CASCADE)
    transaction_date = models.DateField()
    transaction_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=100)
    transaction_status = models.CharField(max_length=100)

    def __str__(self):
        return f"Transaction for {self.rental_reservation}"
