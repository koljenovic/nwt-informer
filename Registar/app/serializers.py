from rest_framework import serializers
from app.models import *


class UlogaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uloga


class GradSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grad


class FirmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firma


class OsobaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Osoba


class VrstaKontaktaSerializer(serializers.ModelSerializer):
    class Meta:
        model = VrstaKontakta


class KontaktSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kontakt


class AdresarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adresar

# class FirmaRegistarSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = FirmaRegistar

# class UserRegistarSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserRegistar

# #Haris
# class AdresarFirmaStavkaRegistarSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = AdresarFirmaStavkaRegistar;

# #Adna
# class KorisnikRegistarSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = KorisnikRegistar;


# class AdresarLiceStavkaRegistarSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = AdresarLiceStavkaRegistar;
