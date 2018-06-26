from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from .views import cabify_home



urlpatterns = [
    url(r'^$',cabify_home,name="home"),
    # url(r'usertype/$',view.setusertype,{})
]