from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.listing, name='listing'),
    url(r'^post/$', views.PostProjectView.as_view(), name='post'),
]