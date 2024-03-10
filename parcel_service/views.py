from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Parcel
from .forms import ParcelForm

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
