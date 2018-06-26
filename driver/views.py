from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import transaction
import datetime as dt
from .models import Driver
from .forms import DriverLocationForm



@login_required(login_url="accounts/login")
def index(request):
    date = dt.date.today()

    if request.method == 'POST':
        form = DriverLocationForm(request.POST)
        if form.is_valid():
            geolocate = form.save(commit=False)
            geolocate.save()
    else:
        form = DriverLocationForm()
        
    return render(request,'driver/index.html', {"date":date , "map_form":form})
