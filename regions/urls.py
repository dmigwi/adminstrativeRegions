from django.conf.urls import url, include
from rest_framework import routers
from regions import views

urlpatterns = [
    url(r'^county/$', views.CountyListView.as_view(), name='countylistview'),
    # <name> -> county
    url(r'^county/(?P<name>\w+)/$', views.CountyMemberView.as_view(), name='countymemberview'),
    url(r'^constituency/$', views.ConstituencyListView.as_view(), name='constituencylistview'),
    # <name> -> constituency
    url(r'^constituency/(?P<name>\w+)/$', views.ConstituencyMemberView.as_view(), name='constituencymemberview'),
    url(r'^ward/$', views.WardListView.as_view(), name='wardlistview'),
    # <name> -> ward
    url(r'^ward/(?P<name>\w+)/$', views.WardMemberView.as_view(), name='wardmemberview'),
]