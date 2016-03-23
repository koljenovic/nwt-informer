from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserRegistar(models.Model):
    #user_django_fk = models.ForeignKey(User, on_delete=models.CASCADE)
    datum_registracije = models.DateTimeField('datum registracije')
    naziv = models.CharField(max_length=200)
    def __str__(self):
        return self.naziv


class FirmaRegistar(models.Model):
    korisnikregistar_fk = models.ForeignKey(UserRegistar, on_delete=models.CASCADE)
    pdv_broj = models.CharField(max_length=200)
    id_broj = models.CharField(max_length=200)
    telefon = models.CharField(max_length=200)
    adresa = models.CharField(max_length=200)
    naziv = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    fax = models.CharField(max_length=200)
    

class KorisnikRegistar(models.Model):
    korisnikregistar_fk = models.ForeignKey(UserRegistar, on_delete=models.CASCADE)
    telefon = models.CharField(max_length=200)
    prezime = models.CharField(max_length=200)
    adresa = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    ime = models.CharField(max_length=200)
    
class AdresarLiceStavkaRegistar(models.Model):
	korisnikregistar_fk = models.ForeignKey(UserRegistar, on_delete=models.CASCADE)
	datum_kreiranja = models.DateTimeField('datum kreiranja')
	dodatne_informacije = models.CharField(max_length=500)
	telefon = models.CharField(max_length=200)
	prezime = models.CharField(max_length=200)
	adresa = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	ime = models.CharField(max_length=200)

class AdresarFirmaStavkaRegistar(models.Model):
	korisnikregistar_fk = models.ForeignKey(UserRegistar, on_delete=models.CASCADE)
	datum_kreiranja = models.DateTimeField('datum kreiranja')
	dodatne_informacije = models.CharField(max_length=500)
	telefon = models.CharField(max_length=200)
	adresa = models.CharField(max_length=200)
	naziv = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
