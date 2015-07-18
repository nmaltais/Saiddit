from django.conf.urls import url
from saidditApp import views

urlpatterns = [
    url('^$', views.homepage),
    url('^login/$', views.loginpage),
    url('^logout/$', views.logoutfunc),
    url('^r/(?P<subsaidditname>\w+)/(?P<postid>[0-9]+)/$', views.viewpostpage),
    url('^r/(?P<subsaidditname>\w+)/$', views.viewsubsaidditpage),
    url('^addpost/(?P<subsaidditname>\w+)/$', views.addpostpage),
    url('^addcomment/(?P<postid>[0-9]+)/$', views.addcommentfunc),
    url('^register/$', views.registerpage),
    url('^postvote/(?P<direction>\w+)/(?P<postid>[0-9]+)/(?P<path>\w+)/$', views.postvotefunc),
    url('^commentvote/(?P<direction>\w+)/(?P<commentid>[0-9]+)/$', views.commentvotefunc),
]
