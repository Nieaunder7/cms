from django.conf.urls import url
from . import views

urlpatterns = [

    #url(r'^ap_add/$',views.ap_create, name='ap_create'),

    #url(r'^stb_update/(?P<pk>\d+)/$',views.STB_UpdateV.as_view(), name='stb_update'),
    #url(r'stb_delete/(?P<pk>\d+)/$',views.STB_DeleteV.as_view(),name='stb_delete'),
    # url(r'^ap_add/$',views.AP_CreateV.as_view(), name='ap_create'),
    # url(r'^ap_update/(?P<pk>\d+)/$',views.AP_UpdateV.as_view(), name='ap_update'),
    # url(r'^ap_delete/(?P<pk>\d+)/$',views.AP_DeleteV.as_view(),name='ap_delete'),
    # url(r'^rc_add/$',views.RC_CreateV.as_view(), name='rc_create'),
    # url(r'^rc_update/(?P<pk>\d+)/$',views.RC_UpdateV.as_view(), name='rc_update'),
    # url(r'^rc_delete/(?P<pk>\d+)/$',views.RC_DeleteV.as_view(),name='rc_delete'),    
    url(r'^device_add/(?P<types>[-\w]+)/$',views.device_add, name='device_create'),
    url(r'^device_update/(?P<types>[-\w]+)/(?P<pk>\d+)/$',views.device_update, name='device_update'),
    url(r'^device_delete/(?P<types>[-\w]+)/(?P<pk>\d+)/$',views.device_delete, name='device_delete'),
    url(r'^$', views.device_list, name='device_list'),

]