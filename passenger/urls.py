from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
import datetime

from . import views


urlpatterns = [
    url(r'^passenger/index$', views.index, name='index'),
]