from django.conf.urls import url
from saidditApp import views

urlpatterns = [
    url('^$', views.homepage),
    url('^login/$', views.loginpage),
    url('^post/(?P<postid>[0-9]+)/$', views.viewpostpage),
    url('^r/(?P<subsaidditname>\w+)/$', views.viewsubsaidditpage),
]
