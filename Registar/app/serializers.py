from rest_framework import serializers
from app.models import * 

class FirmaRegistarSerializer(serializers.ModelSerializer):
    class Meta:
        model = FirmaRegistar

class UserRegistarSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegistar
