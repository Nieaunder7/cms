from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.member_list, name='member_list'),
]