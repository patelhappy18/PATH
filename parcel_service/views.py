from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Parcel, createParcelRide
from .forms import ParcelForm, CreateParcelRideForm, RideSearchForm
from django.http import HttpResponse
def parcel_list(request):
    parcels = Parcel.objects.all()
    return render(request, 'parcel/parcel_list.html', {'parcels': parcels})

def parcel_detail(request, parcel_id):
    parcel = get_object_or_404(Parcel, pk=parcel_id)
    return render(request, 'parcel/parcel_detail.html', {'parcel': parcel})

def create_parcel(request):
    if request.method == 'POST':
        form = ParcelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('parcel_list')
    else:
        form = ParcelForm()
    return render(request, 'parcel/parcel_form.html', {'form': form})

def create_parcel_ride(request):
    if request.method == 'POST':
        form = CreateParcelRideForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
            #return HttpResponse('Your ride is saved.')
    else:
        form = CreateParcelRideForm()
    return render(request, 'parcel/create_parcel_ride.html', {'form': form})


def dashboard(request):
    rides = createParcelRide.objects.all()
    return render(request, 'parcel/dashboard.html', {'rides': rides})

def dashboard_enduser(request):
    rides = createParcelRide.objects.all()
    if request.method == 'POST':
        form = RideSearchForm(request.POST)
        if form.is_valid():
            source = form.cleaned_data['source']
            destination = form.cleaned_data['destination']
            rides = createParcelRide.objects.filter(source=source, destination=destination)
            if not rides:
                message = "No ride found."
            else:
                message = ""
    else:
        form = RideSearchForm()
        message = ""

    return render(request, 'parcel/dashboard_enduser.html', {'rides': rides, 'form': form, 'message': message})