from django.conf.urls import url, include
from django.contrib import admin
from .views import setusertype


urlpatterns = [
    url(r'^usertype$',setusertype,name="setusertype"),
    # url(r'usertype/$',view.setusertype,{})
]
