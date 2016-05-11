from django.shortcuts import render
from app.models import *
from app.serializers import *
from rest_framework import generics
from django.http import HttpResponse
from registration.views import RegistrationView
from app.forms import *
from django.views.generic.edit import FormView
from rest_framework.permissions import AllowAny, DjangoModelPermissions
from drf_haystack.viewsets import HaystackViewSet
from rest_framework.mixins import ListModelMixin
from drf_haystack.generics import HaystackGenericAPIView

def index(request):
    return HttpResponse("Korisnik: " + request.user.username)


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


class KontaktCreate(generics.ListCreateAPIView):
    queryset = Kontakt.objects.all()
    serializer_class = KontaktSerializer


class KontaktDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kontakt.objects.all()
    serializer_class = KontaktSerializer


class AdresarCreate(generics.ListCreateAPIView):
    queryset = Adresar.objects.all()
    serializer_class = AdresarSerializer


class AdresarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Adresar.objects.all()
    serializer_class = AdresarSerializer


    # class FirmaRegistarCreate(generics.ListCreateAPIView):
    #     queryset = FirmaRegistar.objects.all()
    #     serializer_class = FirmaRegistarSerializer

    # class FirmaRegistarDetail(generics.RetrieveUpdateDestroyAPIView):
    #     queryset = FirmaRegistar.objects.all()
    #     serializer_class = FirmaRegistarSerializer

    # class UserRegistarCreate(generics.ListCreateAPIView):
    #     queryset = UserRegistar.objects.all()
    #     serializer_class = UserRegistarSerializer

    # class UserRegistarDetail(generics.RetrieveUpdateDestroyAPIView):
    #     queryset = UserRegistar.objects.all()
    #     serializer_class = UserRegistarSerializer

    # #Haris

    # class AdresarFirmaStavkaRegistarCreate(generics.CreateAPIView):
    #     queryset = AdresarFirmaStavkaRegistar.objects.all()
    #     serializer_class = AdresarFirmaStavkaRegistarSerializer

    # class AdresarFirmaStavkaRegistarDetail(generics.RetrieveUpdateDestroyAPIView):
    #     queryset = AdresarFirmaStavkaRegistar.objects.all()
    #     setializer_class = AdresarFirmaStavkaRegistarSerializer



    # #Adna
    # class KorisnikRegistarDetail(generics.CreateAPIView):
    #     queryset = KorisnikRegistar.objects.all()
    #     serializer_class = KorisnikRegistarSerializer

    # class KorisnikRegistarDetail(generics.RetrieveUpdateDestroyAPIView):
    #     queryset = KorisnikRegistar.objects.all()
    #     serializer_class = KorisnikRegistarSerializer



    # class AdresarLiceStavkaRegistarDetail(generics.CreateAPIView):
    #     queryset = AdresarLiceStavkaRegistar.objects.all()
    #     serializer_class = AdresarLiceStavkaRegistarSerializer

    # class AdresarLiceStavkaRegistarDetail(generics.RetrieveUpdateDestroyAPIView):
    #     queryset = AdresarLiceStavkaRegistar.objects.all()
    #     serializer_class = AdresarLiceStavkaRegistarSerializer
