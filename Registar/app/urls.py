from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.generic import TemplateView
from app.views import *

urlpatterns = [

    # url(r'^$', index, name='index'),
    url(r'^korisnik/((?P<pk>[0-9]+)/)?$', get_user, name='get_user'),
    url(r'^$', TemplateView.as_view(template_name='pages/index.html')),
    url(r'^accounts/profile/$', index),
    # url(r'^index/$', index, name='index'),
    url(r'^api/uloga/$', UlogaCreate.as_view()),
    url(r'^api/uloga/(?P<pk>[0-9]+)/$', UlogaDetail.as_view()),
    url(r'^api/user/(?P<pk>[0-9]+)/$', UserDetail.as_view()),
    url(r'^api/user/(?P<username>[a-zA-Z]+)/$', UserDetail_ByUsername.as_view()),
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
    url(r'^part/firma/$', TemplateView.as_view(template_name='parts/firma.html')),
    url(r'^part/profil/$', TemplateView.as_view(template_name='parts/profil.html')),
    url(r'^part/search/$', TemplateView.as_view(template_name='parts/search.html')),
    url(r'^part/kontakt/novi/$', TemplateView.as_view(template_name='parts/kontakt_novi.html')),
    url(r'^part/kontaktosoba/novi/$', TemplateView.as_view(template_name='parts/kontaktosoba_novi.html')),
    url(r'^search/', FirmaSearchView.as_view()),
    url(r'^api/tim/$', TimCreate.as_view()),
    url(r'^api/uloga/(?P<pk>[0-9]+)/$', UlogaDetail.as_view()),
    url(r'^api/uloga/$', UlogaCreate.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
