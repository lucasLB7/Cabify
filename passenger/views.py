from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import transaction

@login_required(login_url="accounts/login")
def index(request):
    return render(request,'passenger/index.html')


# # @login_required
# def passenger_profile(request):
#     user=User.objects.get_or_create(id=requets.user.id)
#     all_details = Driver.objects.get(user=user)
#     prof_details = {"user_details":all_details}

#     return render(request, 'user_profile.html', prof_details )





# # @login_required
# @transaction.atomic
# def update_passenger_profile(request):
#     if request.method == 'POST':
#         user_form = UserForm(request.POST, instance=request.user)
#         profile_form = ProfileForm(request.POST, instance=request.user.profile)
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, _('Your profile was successfully updated!'))
#             return redirect('settings:profile')
#         else:
#             messages.error(request, _('Please correct the error below.'))
#     else:
#         user_form = UserForm(instance=request.user)
#         profile_form = ProfileForm(instance=request.user.profile)
#     return render(request, 'profiles/profile.html', {
#         'user_form': user_form,
#         'profile_form': profile_form
#     })
