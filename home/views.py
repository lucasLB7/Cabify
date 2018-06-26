from django.shortcuts import render



def cabify_home(request):
    title = "Cabify maps HOME"
    



    return render(request, "homepage/home_main.html", {"title":title})
