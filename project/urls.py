from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^add/$',views.project_add, name='project_add'),
    url(r'^update/(?P<pk>\d+)/$',views.project_update, name='project_update'),
    url(r'^delete/(?P<pk>\d+)/$',views.project_delete, name='project_delete'),
    url(r'^$', views.project_list, name='project_list'),
]