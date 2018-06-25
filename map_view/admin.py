from django.contrib import admin

from .models import Incidences, Profile, Location


class IncidencesAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')

# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('bio', 'location')
    

# Register your models here.
admin.site.register(Incidences, IncidencesAdmin)
admin.site.register(Profile)
admin.site.register(Location)