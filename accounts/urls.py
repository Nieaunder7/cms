from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    url(r'^login/$', auth_views.LoginView.as_view(), name='login'),
    url(r'^logout/$',auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    url(r'^register/$', register, name = 'register'),
]