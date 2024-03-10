from django import forms
from .models import Parcel

class ParcelForm(forms.ModelForm):
    class Meta:
        model = Parcel
        fields = ['sender', 'recipient', 'source', 'destination', 'description', 'weight', 'delivery_date']
