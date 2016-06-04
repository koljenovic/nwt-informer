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


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail_ByUsername(generics.RetrieveAPIView):
    queryset = User.objects.all()
    lookup_field = 'username'
    serializer_class = UserSerializer


class UlogaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Uloga.objects.all()
    serializer_class = UlogaSerializer


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


class FirmaSearchView(ListModelMixin, HaystackGenericAPIView):
    # index_models = [Firma]

    serializer_class = FirmaIndexSerializer
      

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
    
    
class UlogaDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Uloga.objects.all()
    serializer_class = UlogaSerializer  
    lookup_field = 'user_fk'  

class UlogaCreate(generics.ListCreateAPIView):
    queryset = Uloga.objects.all()
    serializer_class = UlogaSerializer  
       
    
class KontaktCreate(generics.ListCreateAPIView):
    queryset = Kontakt.objects.all()
    serializer_class = KontaktSerializer
    paginate_by = 100
    paginate_by_param = 'page_size'
    max_paginate_by = 500
    



class KontaktDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kontakt.objects.all()
    serializer_class = KontaktSerializer
    

class AdresarCreate(generics.ListCreateAPIView):
    queryset = Adresar.objects.all()
    serializer_class = AdresarSerializer


class AdresarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Adresar.objects.all()
    serializer_class = AdresarSerializer
