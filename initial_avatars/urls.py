from django.conf.urls import  include, url

urlpatterns = [ 
	url(r'^avatar/(?P<username>\w+(?:(?:\+|\.|-)\w+)*)/$', 'initial_avatars.views.avatar', name='avatar'),
	url(r'^avatar/(?P<username>\w+(?:(?:\+|\.|-)\w+)*)/(?P<size>[0-9]{2,3})/$', 'initial_avatars.views.avatar', name='avatar'),
]