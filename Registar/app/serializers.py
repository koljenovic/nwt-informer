from rest_framework import serializers
from app.models import *
from app.search_indexes import *
from drf_haystack.serializers import HaystackSerializer


class UlogaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uloga


class GradSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grad


class FirmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firma


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class FirmaIndexSerializer(HaystackSerializer):
    class Meta:
        index_classes = [FirmaIndex]
        fields = ['text', 'naziv', 'id']


class OsobaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Osoba


class VrstaKontaktaSerializer(serializers.ModelSerializer):
    class Meta:
        model = VrstaKontakta


class KontaktSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kontakt


class TimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kontakt
        fields = ['id', 'osoba_fk', 'kontakt', 'vrsta_fk']
        
		
class AdresarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adresar
