from django.contrib import admin
from.models import Parcel,createParcelRide, ParcelService, Location, UserActivity
# Register your models here.
admin.site.register(Parcel)
admin.site.register(createParcelRide)
admin.site.register(ParcelService)
admin.site.register(Location)
admin.site.register(UserActivity)