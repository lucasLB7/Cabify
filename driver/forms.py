from django import forms
from .models import DriverLocation, Driver
from django_google_maps.widgets import GoogleMapsAddressWidget

class DriverLocationForm(forms.ModelForm):
    class Meta:
        model = DriverLocation
        fields = '__all__'
        widgets = {
            'address': GoogleMapsAddressWidget,
        }


class DriverProfileForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = '__all__'
       

    
