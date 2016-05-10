from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.generic import TemplateView
from app.views import *

urlpatterns = [

    url(r'^$', index, name='index'),
    url(r'^accounts/profile/$', index),
    # url(r'^firmaregistar/$', views.FirmaRegistarCreate.as_view()),
    # url(r'^firmaregistar/(?P<pk>[0-9]+)/$', views.FirmaRegistarDetail.as_view()),
    # url(r'^userregistar/$', views.UserRegistarCreate.as_view()),
    # url(r'^userregistar/(?P<pk>[0-9]+)/$', views.UserRegistarDetail.as_view()),
    url(r'^index/$', index, name='index'),
    # url(r'^adresarfirmastavkaregistar/$', views.AdresarFirmaStavkaRegistarCreate.as_view()),
    # url(r'^adresarfirmastavkaregistar/(?P<px>[0-9]+)/$', views.AdresarFirmaStavkaRegistarDetail.as_view()),
    # url(r'^korisnikregistar/$', views.KorisnikRegistarDetail.as_view()),
    # url(r'^korisnikregistar/(?P<pk>[0-9]+)/$', views.KorisnikRegistarDetail.as_view()),
    # url(r'^adresarlicestavkaregistar/$', views.AdresarLiceStavkaRegistarDetail.as_view()),
    # url(r'^adresarlicestavkaregistar/(?P<pk>[0-9]+)/$', views.AdresarLiceStavkaRegistarDetail.as_view()),
    url(r'^api/uloga/$', UlogaCreate.as_view()),
    url(r'^api/uloga/(?P<pk>[0-9]+)/$', UlogaDetail.as_view()),
    url(r'^api/grad/$', GradCreate.as_view()),
    url(r'^api/grad/(?P<pk>[0-9]+)/$', GradDetail.as_view()),
    url(r'^api/firma/$', FirmaCreate.as_view()),
    url(r'^api/firma/(?P<pk>[0-9]+)/$', FirmaDetail.as_view()),
    url(r'^api/osoba/$', OsobaCreate.as_view()),
    url(r'^api/osoba/(?P<pk>[0-9]+)/$', OsobaDetail.as_view()),
    url(r'^api/vrstakontakta/$', VrstaKontaktaCreate.as_view()),
    url(r'^api/vrstakontakta/(?P<pk>[0-9]+)/$', VrstaKontaktaDetail.as_view()),
    url(r'^api/kontakt/$', KontaktCreate.as_view()),
    url(r'^api/kontakt/(?P<pk>[0-9]+)/$', KontaktDetail.as_view()),
    url(r'^api/adresar/$', AdresarCreate.as_view()),
    url(r'^api/adresar/(?P<pk>[0-9]+)/$', AdresarDetail.as_view()),
    url(r'^osoba/$', OsobaFormView.as_view()),
    url(r'^firma/$', TemplateView.as_view(template_name='parts/firma.html')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
