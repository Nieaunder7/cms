from django.conf.urls import url
from . import views

urlpatterns = [  
    url(r'^device_add/(?P<types>[-\w]+)/$',views.device_add, name='device_create'),
    url(r'^device_update/(?P<types>[-\w]+)/(?P<pk>\d+)/$',views.device_update, name='device_update'),
    url(r'^device_delete/(?P<types>[-\w]+)/(?P<pk>\d+)/$',views.device_delete, name='device_delete'),
    url(r'^$', views.device_list, name='device_list'),
]