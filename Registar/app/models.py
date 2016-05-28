from __future__ import unicode_literals

import datetime

from django.core.validators import validate_email
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User

from registration.signals import user_activated
from django.dispatch import receiver

# Preset lista gradova
class Grad(models.Model):
    naziv = models.CharField(max_length=50)
    postanski_broj = models.CharField(max_length=10)

    def __str__(self):
        return self.naziv


class Firma(models.Model):
    # @TODO: mozda dodati reputaciju, korisnici ostavljaju star rating, datum registracije?
    alias = models.CharField(max_length=50, null=True)
    naziv = models.CharField(max_length=200)
    opis = models.CharField(max_length=500, default='')
    adresa = models.CharField(max_length=200)
    admin_fk = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    grad_fk = models.ForeignKey(Grad, on_delete=models.CASCADE, null=True, blank=True)
    pdv_broj = models.CharField(max_length=25)
    id_broj = models.CharField(max_length=25)
    logo = models.CharField(max_length=250, default='', null=True, blank=True)

    def clean(self):
        if self.alias is None:
            raise ValidationError(_('Alias je obavezno polje.'))
        if self.naziv is None:
            raise ValidationError(_('Naziv je obavezno polje.'))
        if self.adresa is None:
            raise ValidationError(_('Adresa je obavezno polje.'))
        if self.pdv_broj is None:
            raise ValidationError(_('PDV broj je obavezno polje.'))
        if self.id_broj is None:
            raise ValidationError(_('ID broj je obavezno polje.'))

    def __str__(self):
        return self.naziv


class Uloga(models.Model):
    firma_fk = models.ForeignKey(Firma, on_delete=models.CASCADE)
    user_fk = models.ForeignKey(User, on_delete=models.CASCADE)
    naziv_uloge = models.CharField(max_length=100)

    def clean(self):
        if self.naziv_uloge is None:
            raise ValidationError(_('Naziv uloge je obavezno polje.'))

    def __str__(self):
        return self.naziv_uloge

@receiver(user_activated)
def osoba_create_callback(sender, **kwargs):
    user = kwargs.get('user')
    if not Osoba.objects.get(id=user.id):
        Osoba.objects.create(id=user.id, user_fk=user, ime='', prezime='').save()

class Osoba(models.Model):
    user_fk = models.ForeignKey(User, on_delete=models.CASCADE)
    ime = models.CharField(max_length=50)
    prezime = models.CharField(max_length=50)

    def clean(self):
        if self.ime is None:
            raise ValidationError(_('Ime je obavezno polje.'))
        if self.prezime is None:
            raise ValidationError(_('Prezime je obavezno polje.'))

    def get_fields(self):
        return {
            'id': self.id,
            'username': self.user_fk.username,
            'email': self.user_fk.email,
            'ime': self.ime,
            'prezime': self.prezime,
            #'slika': self.slika,
            'super': self.user_fk.is_superuser,
            'staff': self.user_fk.is_staff,
            }

    def __str__(self):
        return str(self.user_fk) + ". " + self.ime + " " + self.prezime

# Preset enumerirane vrijednosti
class VrstaKontakta(models.Model):
    vrsta_kontakta = models.CharField(max_length=100)
    
    def __str__(self):
        return self.vrsta_kontakta

class Kontakt(models.Model):
    osoba_fk = models.ForeignKey(Osoba, on_delete=models.CASCADE)
    firma_fk = models.ForeignKey(Firma, on_delete=models.CASCADE)
    vrsta_fk = models.ForeignKey(VrstaKontakta, on_delete=models.CASCADE)
    kontakt = models.CharField(max_length=250)

    def clean(self):
        if self.kontakt is None:
            raise ValidationError(_('Kontakt je obavezno polje.'))


class Adresar(models.Model):
    osoba_fk = models.ForeignKey(Osoba, on_delete=models.CASCADE)
    kontakt_fk = models.ForeignKey(Kontakt, on_delete=models.CASCADE)


class Slika(models.Model):
    osoba_fk = models.ForeignKey(Osoba, on_delete=models.CASCADE, null=True)
    firma_fk = models.ForeignKey(Firma, on_delete=models.CASCADE, null=True)
    slika = models.ImageField(upload_to='myphoto/', null=True, max_length=255)