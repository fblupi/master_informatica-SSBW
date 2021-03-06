from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list/$', views.list, name='list'),
    url(r'^search/$', views.search, name='search'),
    url(r'^add/$', views.add, name='add'),
    url(r'^restaurant/(?P<id>[0-9]+)$', views.restaurant, name='restaurant'),
    url(r'^images/(?P<id>[0-9]+)$', views.show_image, name='show_image'),
    url(r'^number/$', views.number_of_restaurants, name='number_of_restaurants'),
]
