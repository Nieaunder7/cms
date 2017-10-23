from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.report_list, name='report_list'),
]