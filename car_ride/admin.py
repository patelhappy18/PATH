from django.contrib import admin

from .models import RegisterDriver, CarType, Location

admin.site.register(RegisterDriver)
admin.site.register(CarType)
admin.site.register(Location)