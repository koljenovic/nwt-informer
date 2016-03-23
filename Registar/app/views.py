from django.shortcuts import render
from app.models import *
from app.serializers import *
from rest_framework import generics

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("INDEX PAGE")

class FirmaRegistarCreate(generics.ListCreateAPIView):
    queryset = FirmaRegistar.objects.all()
    serializer_class = FirmaRegistarSerializer

class FirmaRegistarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FirmaRegistar.objects.all()
    serializer_class = FirmaRegistarSerializer

class UserRegistarCreate(generics.ListCreateAPIView):
    queryset = UserRegistar.objects.all()
    serializer_class = UserRegistarSerializer

class UserRegistarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserRegistar.objects.all()
    serializer_class = UserRegistarSerializer

#Haris

class AdresarFirmaStavkaRegistarCreate(generics.CreateAPIView):
    queryset = AdresarFirmaStavkaRegistar.objects.all()
    serializer_class = AdresarFirmaStavkaRegistarSerializer

class AdresarFirmaStavkaRegistarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AdresarFirmaStavkaRegistar.objects.all()
    setializer_class = AdresarFirmaStavkaRegistarSerializer



#Adna
class KorisnikRegistarDetail(generics.CreateAPIView):
	queryset = KorisnikRegistar.objects.all()
	serializer_class = KorisnikRegistarSerializer

class KorisnikRegistarDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = KorisnikRegistar.objects.all()
	serializer_class = KorisnikRegistarSerializer



class AdresarLiceStavkaRegistarDetail(generics.CreateAPIView):
	queryset = AdresarLiceStavkaRegistar.objects.all()
	serializer_class = AdresarLiceStavkaRegistarSerializer

class AdresarLiceStavkaRegistarDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = AdresarLiceStavkaRegistar.objects.all()
	serializer_class = AdresarLiceStavkaRegistarSerializer

