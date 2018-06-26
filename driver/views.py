from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import transaction
import datetime as dt

@login_required(login_url="accounts/login")
def index(request):
    date = dt.date.today()
    return render(request,'driver/index.html', {"date":date})
