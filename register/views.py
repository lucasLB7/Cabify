from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from passenger.models import Passenger
from driver.models import Driver
from driver.forms import DriverProfileForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

# /////////////////////////////////////////////////////////////////////


@login_required(login_url="accounts/login")
def index(request):
    user=User.objects.get(id=request.user.id)
    #try to get profile
    driver_users=[x.user for x in Driver.objects.all()]
    passenger_users=[x.user for x in Passenger.objects.all()]

    if user in driver_users:
        return redirect('driver:index', user_id=3)

    if user in passenger_users:
        return redirect('passenger:index')

    return redirect('register:newprofile')

# /////////////////////////////////////////////////////////////////////

@login_required(login_url="accounts/login")
def create_profile(request):


    if request.method == 'POST':
        profile_form = DriverProfileForm(request.POST)
        if profile_form.is_valid():

            updatedriver = form.save(commit = False)
            updatedriver.save()
    else:

        profile_form = DriverProfileForm()
        

    return render(request,'registration/select_account_type.html', {"profile_form":profile_form})

# /////////////////////////////////////////////////////////////////////

@login_required(login_url="accounts/login")
def create_driver(request):
    user=User.objects.get(id=request.user.id)
    driver=Driver(user=user)
    driver.save()
    return redirect("register:index")

# /////////////////////////////////////////////////////////////////////

@login_required(login_url="accounts/login")
def create_passenger(request):
    user=User.objects.get(id=request.user.id)
    passenger=Passenger(user=user)
    passenger.save()
    return redirect("register:index")

# /////////////////////////////////////////////////////////////////////


@login_required(login_url="accounts/login")
def new_user_form(request, user_id):

    if request.method == "POST":
        new_user_form = DriverProfieForm(request.POST)
        if map_form.is_valid() or profile_form.is_valid():


            updatedriver = form.save(commit = False)
            updatedriver.save()
    else:
        new_user_form = DriverProfileForm()


# /////////////////////////////////////////////////////////////////////