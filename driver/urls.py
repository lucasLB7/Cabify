from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
import datetime

from . import views


urlpatterns = [
    url(r'^driver/index/(?P<user_id>\d+)$', views.index, name='index'),
    # url(r'^driver/update_profile/(?P<user_id>\d+)$', views.index, name='index'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)