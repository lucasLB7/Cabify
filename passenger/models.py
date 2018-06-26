from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from django.dispatch import receiver


import datetime as dt


from django.contrib.gis.geos import Point
from django.contrib.gis.db import models as gis_models
from location_field.models.spatial import LocationField

from pyuploadcare.dj.models import ImageField


# ///////////////////////////////////////////////////////////////


class Passenger(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    # location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(blank=True)
    
    

    # @receiver(post_save, sender=User)
    # def create_passenger_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Passenger.objects.create(user=instance)

    # @receiver(post_save, sender=User)
    # def save_passenger_profile(sender, instance, **kwargs):
    #     instance.passenger.save()

    # @receiver(post_save, sender=User)
    # def delete_passenger_profile(sender, instance, **kwargs):
    #     instance.passenger.delete()
    
    # @classmethod
    # def all_passenger_details(cls):
    #     details = cls.objects.all()


    class Meta:
        ordering = ['user']



# ///////////////////////////////////////////////////////////////
# class PassengerLocation(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     city = models.CharField(max_length=255)
#     location = LocationField(based_fields=['city'], zoom=7, default=Point(1.0, 1.0))
#     # objects = gis_models.GeoManager()

