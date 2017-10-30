from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^add/$',views.testcase_add, name='testcase_add'),
    url(r'update/(?P<pk>\d+)/$',views.testcase_update, name='testcase_update'),
    url(r'delete/(?P<pk>\d+)/$',views.testcase_delete, name='testcase_delete'),
    url(r'^$',views.testCase_list, name='testcase_list'),
]