from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list/$', views.list, name='list'),
    url(r'^search/$', views.search, name='search'),
    url(r'^add/$', views.add, name='add'),
    url(r'^restaurant/(?P<id>[0-9]+)$', views.restaurant, name='restaurant'),
]
