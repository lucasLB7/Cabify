from django.db import models
from django.contrib.auth.models import User
import datetime as dt


from django.contrib.gis.geos import Point
from django.contrib.gis.db import models as gis_models
from location_field.models.spatial import LocationField
from pyuploadcare.dj.models import ImageField

from django_google_maps import fields as map_fields



# ///////////////////////////////////////////////////////////////

class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30,blank=True)
    last_name = models.CharField(max_length=30,blank=True)
    phone_number = models.IntegerField(null=True,blank=True)
    national_id = models.IntegerField(null=True,blank=True)
    profile_picture = models.ImageField(blank=True, upload_to="profile_images/", default='profile_images/default_image.png')

    class Meta:
        ordering = ['user']

    @classmethod
    def get_all_details_by_id(cls, id):
        all_details = Driver.objects.get(pk=id)
        return all_details
    
    # @classmethod
    # def get_prof_pic_by_id(cls, id):
    #     prof_pic = Driver.objects.get(pk=id)
    #     return prof_pic

    # @classmethod
    # def get_all_details_by_id(cls, id):
    #     all_details = Driver.objects.

# ///////////////////////////////////////////////////////////////


# ///////////////////////////////////////////////////////////////


class Car(models.Model):
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    production_year = models.DateField()
    licence_plate = models.CharField(max_length=7)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE,blank=True,null=True, related_name="car")

    




class DriverLocation(models.Model):

    address = map_fields.AddressField(max_length=200, blank=True)
    geolocation = map_fields.GeoLocationField(max_length=100, blank=True)

    def __str__(self):
        return self.address

   



# ///////////////////////////////////////////////////////////////


# class DriverRating(models.Model):
#     driver=models.OneToOneField(Driver)
#     stars=models.IntegerField()
#     review=models.CharField(max_length=255)






# # ///////////////////////////////////////////////////////////////
# class DriverLocation(models.Model):
#     driver = models.OneToOneField(Driver, on_delete=models.CASCADE)
#     city = models.CharField(max_length=255)
#     # location = LocationField(based_fields=['city'], zoom=7, default=Point(1.0, 1.0))
#     # objects = gis_models.GeoManager()