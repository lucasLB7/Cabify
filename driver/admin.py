from django.contrib import admin
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields
from django.forms.widgets import TextInput
from django_google_maps.widgets import GoogleMapsAddressWidget
from django_google_maps.fields import AddressField, GeoLocationField


from .models import DriverLocation, Driver, Car




class DriverAdmin(admin.ModelAdmin):
    formfield_overrides = {
        AddressField:{
            'widget': GoogleMapsAddressWidget
        },
        GeoLocationField:{
            'widget': TextInput(attrs={
                'readonly':'readonly'
            })
        }
    }
    

admin.site.register(DriverLocation, DriverAdmin)
admin.site.register(Driver)
admin.site.register(Car)




# from .models import Driver, DriverLocation, DriverRating, Car


# class DriverAdmin(admin.ModelAdmin):
#     filter_horizontal = ('driverlocation' ,'car')

# admin.site.register(DriverLocation)
# admin.site.register(Car)

