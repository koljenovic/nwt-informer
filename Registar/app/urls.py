from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^firmaregistar/$', views.FirmaRegistarCreate.as_view()),
    url(r'^firmaregistar/(?P<pk>[0-9]+)/$', views.FirmaRegistarDetail.as_view()),
    url(r'^userregistar/$', views.UserRegistarCreate.as_view()),
    url(r'^userregistar/(?P<pk>[0-9]+)/$', views.UserRegistarDetail.as_view()),
    url(r'^index/$', views.index, name='index'),
    url(r'^adresarfirmastavkaregistar/$', views.AdresarFirmaStavkaRegistarCreate.as_view()),
    url(r'^adresarfirmastavkaregistar/(?P<px>[0-9]+)/$', views.AdresarFirmaStavkaRegistarDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)