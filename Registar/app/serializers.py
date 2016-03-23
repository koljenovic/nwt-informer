from rest_framework import serializers
from app.models import * 

class FirmaRegistarSerializer(serializers.ModelSerializer):
    class Meta:
        model = FirmaRegistar

class UserRegistarSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegistar

#Haris
class AdresarFirmaStavkaRegistarSerializer(serializers.ModelSerializer):
	class Meta:
		model = AdresarFirmaStavkaRegistar;

#Adna
class KorisnikRegistarSerializer(serializers.ModelSerializer):
	class Meta:
		model = KorisnikRegistar;
    

class AdresarLiceStavkaRegistarSerializer(serializers.ModelSerializer):
	class Meta:
		model = AdresarLiceStavkaRegistar;
