from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib.auth import views as authviews

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^createuserprofile$',views.create_profile,name="newprofile"),
    url(r'^createpassenger$',views.create_passenger,name="create-passenger"),
    url(r'^createdriver$',views.create_driver,name="create-driver"),
    url(r"^logout",authviews.logout,{"next_page":'/'},name="logout"),
]