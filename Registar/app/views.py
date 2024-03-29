from django.shortcuts import render
from app.models import *
from app.serializers import *
from rest_framework import generics
from django.http import HttpResponse
from registration.backends.default.views import RegistrationView
from app.forms import *
from django.views.generic.edit import FormView
from rest_framework.permissions import AllowAny, DjangoModelPermissions
from drf_haystack.viewsets import HaystackViewSet
from rest_framework.mixins import ListModelMixin
from drf_haystack.generics import HaystackGenericAPIView
import json
from django.contrib.auth import logout
from django.core.paginator import Paginator
from rest_framework.pagination import PageNumberPagination

def index(request):
    return HttpResponse()


def get_user(request, **kwargs):
    pk = kwargs.get('pk')
    pk = pk if pk else request.user.id
    osoba = None
    user = None
    try:
        osoba = Osoba.objects.get(id=pk)
    except Exception, e:
        try:
            user = User.objects.get(id=pk)
        except Exception, e:
            pass
    return HttpResponse(json.dumps({'korisnik': osoba.get_fields() if osoba else { 'username': user.username, 'id': user.id } if user else None }))
    
    
def get_userid(request):
	if request.user.is_authenticated():
		return HttpResponse(json.dumps({'result': {'logged': True}, 'user': request.user.id}), content_type="application/json")
	else:
		return HttpResponse(json.dumps({'result': {'logged': False}}), content_type="application/json")

    

class RegisterView(RegistrationView):
    template_name = 'registration/register.html'
    form_class = RegistrationCaptcha

class FirmaFormView(FormView):
    template_name = 'forms/generic.html'
    form_class = FirmaForm


class OsobaFormView(FormView):
    template_name = 'forms/generic.html'
    form_class = OsobaForm


class UlogaCreate(generics.ListCreateAPIView):
    queryset = Uloga.objects.all()
    serializer_class = UlogaSerializer
    
class UlogaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Uloga.objects.all()
    serializer_class = UlogaSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail_ByUsername(generics.RetrieveAPIView):
    queryset = User.objects.all()
    lookup_field = 'username'
    serializer_class = UserSerializer

class GradCreate(generics.ListCreateAPIView):
    queryset = Grad.objects.all()
    serializer_class = GradSerializer


class GradDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Grad.objects.all()
    serializer_class = GradSerializer


class FirmaCreate(generics.ListCreateAPIView):
    queryset = Firma.objects.all()
    serializer_class = FirmaSerializer


class FirmaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Firma.objects.all()
    serializer_class = FirmaSerializer


class SearchPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 500

class FirmaSearchView(ListModelMixin, HaystackGenericAPIView):
    # index_models = [Firma]

    serializer_class = FirmaIndexSerializer
    pagination_class = SearchPagination

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class OsobaCreate(generics.ListCreateAPIView):
    queryset = Osoba.objects.all()
    serializer_class = OsobaSerializer


class OsobaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Osoba.objects.all()
    serializer_class = OsobaSerializer


class VrstaKontaktaCreate(generics.ListCreateAPIView):
    queryset = VrstaKontakta.objects.all()
    serializer_class = VrstaKontaktaSerializer


class VrstaKontaktaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = VrstaKontakta.objects.all()
    serializer_class = VrstaKontaktaSerializer


class TimCreate(generics.ListAPIView):
    queryset = Kontakt.objects.all()
    serializer_class = TimSerializer


class KontaktCreate(generics.ListCreateAPIView):
    queryset = Kontakt.objects.all()
    serializer_class = KontaktSerializer


class KontaktList_ByOsobaId(generics.ListAPIView):
    lookup_field = 'osoba_fk'
    serializer_class = KontaktSerializer

    def get_queryset(self):
        osoba_fk = self.kwargs['osoba_fk']
        return Kontakt.objects.filter(osoba_fk__id=osoba_fk)


class UlogaList_ByUserId(generics.ListAPIView):
    lookup_field = 'user_fk'
    serializer_class = UlogaSerializer

    def get_queryset(self):
        user_fk = self.kwargs['user_fk']
        return Uloga.objects.filter(user_fk__id=user_fk)


class KontaktDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kontakt.objects.all()
    serializer_class = KontaktSerializer

    
class AdresarCreate(generics.ListCreateAPIView):
    queryset = Adresar.objects.all()
    serializer_class = AdresarSerializer


class AdresarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Adresar.objects.all()
    serializer_class = AdresarSerializer
