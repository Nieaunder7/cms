from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^add/$',views.project_add, name='project_add'),
    url(r'^$', views.project_list, name='project_list'),
]