from django.urls import path
from . import views

urlpatterns = [
    path('', views.parcel_list, name='parcel_list'),
    path('parcel/<int:parcel_id>/', views.parcel_detail, name='parcel_detail'),
    path('parcel/new/', views.create_parcel, name='create_parcel'),
]
