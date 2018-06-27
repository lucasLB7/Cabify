from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import transaction
import datetime as dt
from .models import Driver
from .forms import DriverLocationForm, DriverProfileForm



@login_required(login_url="accounts/login")
def index(request):
    date = dt.date.today()

    if request.method == 'POST':
        map_form = DriverLocationForm(request.POST)
        profile_form = DriverProfileForm(request.POST)
        if map_form.is_valid() or profile_form.is_valid():

            geolocate = form.save(commit=False)
            geolocate.save()

            updatedriver = form.save(commit = False)
            updatedriver.save()
    else:
        map_form = DriverLocationForm()
        profile_form = DriverProfileForm()
        
    return render(request,'driver/index.html', {"date":date , "map_form":map_form , "profile_form": profile_form})




# @login_required(login_url="accounts/login")
# def updateProfile(request):

#     if request.method == 'POST':
#         form = DriverProfileForm(request.POST)
#         if form.is_valid():
#             updatedriver = form.save(commit = False)
#             updatedriver.save()
#     else:
#         form = DriverProfileForm()
#     return render(request, 'driver/index.html' , {"form":form})


# def multiple_forms(request):
#     if request.method == 'POST':
#         contact_form = ContactForm(request.POST)
#         subscription_form = SubscriptionForm(request.POST)
#         if contact_form.is_valid() or subscription_form.is_valid():
#             # Do the needful
#             return HttpResponseRedirect(reverse('form-redirect') )
#     else:
#         contact_form = ContactForm()
#         subscription_form = SubscriptionForm()

#     return render(request, 'pages/multiple_forms.html', {
#         'contact_form': contact_form,
#         'subscription_form': subscription_form,
#     })