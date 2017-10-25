from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^add/$',views.member_add, name='member_add'),
    url(r'^update/(?P<pk>\d+)/$',views.member_update, name ='member_update'),
    url(r'^delete/(?P<pk>\d+)/$',views.member_delete, name = 'member_delete'),
    url(r'^$', views.member_list, name='member_list'),
]