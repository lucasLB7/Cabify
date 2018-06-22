from django.shortcuts import render



def cabify_home(request):
    return render(request, "homepage/home_main.html")
