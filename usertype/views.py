from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import ChooseForm
from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required
def setusertype(request):
    user=User.objects.get(id=request.user.id)
    if request.method=="POST":
        form=ChooseForm(request.Post)
        if form.is_valid():
            choice=form.cleaned_data['choice']
            print(choice)

            return render(request,'usertype/usertype.html',form)

    
    else:
        form=ChooseForm()
        return render(request,'usertype/usertype.html',form)

