from __future__ import unicode_literals
from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from tinymce.models import HTMLField
import datetime as dt
from django.db.models.signals import post_save
from django.dispatch import receiver


class Location(models.Model):
    pass

class Profile(BaseUserManager):
    HABITATION_TYPE = (
        ('Appartment','Appartment'),
        ('Bedsitter', 'Bedsitter'),
        ('Home with garden'),

    )

    user = models.OneToOneField(User, default = 1, on_delete=models.CASCADE)
    bio = models.CharField(max_length=30, blank = True)
    location = models.CharField(max_length=255, blank = True)
    birth_day = models.DateField(null = True, blank = True)
    career = models.CharField(max_length=250, blank = True)
    habitation = models.CharField(max_length=30, choice=HABITATION_TYPE, default="Appartment")


    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now= True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.created(user = instance)

@receiver(post_save, sender = User)
def save_user_profile(sender, instance, created, **kwargs):
    instance.profile.save()

class Incidences(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    # user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name
    

    class Meta:
        verbose_name_plural = 'Incidences'
