from django import forms
from .models import Parcel, createParcelRide

class ParcelForm(forms.ModelForm):
    class Meta:
        model = Parcel
        fields = ['sender', 'recipient', 'source', 'destination', 'description', 'weight']

class CreateParcelRideForm(forms.ModelForm):
    class Meta:
        model = createParcelRide
        fields = ['username', 'source', 'destination', 'description']

class RideSearchForm(forms.Form):
    CHOICES = [(city, city) for city in
               ['Toronto', 'Montreal', 'Vancouver', 'Calgary', 'Edmonton', 'Ottawa', 'Winnipeg', 'Quebec City',
                'Hamilton', 'London', 'Kitchener', 'St. Catharines', 'Halifax', 'Oshawa', 'Victoria', 'Windsor',
                'Saskatoon', 'Regina', 'Barrie', 'St. John\'s', 'Kelowna', 'Sherbrooke', 'Trois-Rivières', 'Guelph',
                'Kingston', 'Moncton', 'Sudbury', 'Brampton', 'Thunder Bay', 'Peterborough', 'Lethbridge', 'Kamloops',
                'Nanaimo', 'Belleville', 'Sarnia', 'Saint John', 'Chatham-Kent', 'Red Deer', 'Kawartha Lakes',
                'Cape Breton', 'Lethbridge', 'Kamloops', 'Nanaimo', 'Belleville', 'Sarnia', 'Saint John',
                'Chatham-Kent', 'Red Deer', 'Kawartha Lakes', 'Cape Breton']]
    source = forms.CharField(label='Source', widget=forms.Select(choices=CHOICES))
    destination = forms.CharField(label='Destination', widget=forms.Select(choices=CHOICES))