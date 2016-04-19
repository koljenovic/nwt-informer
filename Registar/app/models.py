from __future__ import unicode_literals
import datetime
from django.core.validators import validate_email
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
def ValidateEmail( email ):    
    try:
        validate_email( email )
        return True
    except ValidationError:
        return False

class UserRegistar(models.Model):
    #user_django_fk = models.ForeignKey(User, on_delete=models.CASCADE)
    datum_registracije = models.DateTimeField('datum registracije')
    naziv = models.CharField(max_length=200)
    def __str__(self):
        return self.naziv
    def clean(self):
        if self.naziv is None:
            raise ValidationError(_('Korisnik mora imati Naziv!!!'))
        if self.datum_registracije is None:
            self.datum_registracije = datetime.date.today()

class FirmaRegistar(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    korisnikregistar_fk = models.ForeignKey(UserRegistar, on_delete=models.CASCADE)
    pdv_broj = models.CharField(max_length=200)
    id_broj = models.CharField(max_length=200)
    telefon = models.CharField(max_length=15,validators=[phone_regex])
    adresa = models.CharField(max_length=200)
    naziv = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    fax = models.CharField(max_length=200)
    def clean(self):
        #ovdje treba dodati regex validatore
        if self.fax is None:
            raise ValidationError(_('Korisnik mora imati pdv broj!!!'))
        if self.naziv is None:
            raise ValidationError(_('Korisnik mora imati pdv broj!!!'))            
        if self.email is not None and ValidateEmail(self.email):
            raise ValidationError(_('Neispravan email!!!'))    

class KorisnikRegistar(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    korisnikregistar_fk = models.ForeignKey(UserRegistar, on_delete=models.CASCADE)
    telefon = models.CharField(max_length=15,validators=[phone_regex])
    prezime = models.CharField(max_length=200)
    adresa = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    ime = models.CharField(max_length=200)
    def clean(self):
        #ovdje treba dodati regex validatore
        if self.adresa is None:
            raise ValidationError(_('Korisnik mora imati adresu!!!'))
        if self.ime is None:
            raise ValidationError(_('Korisnik mora imati ime!!!'))            
        if self.email is not None and ValidateEmail(self.email):
            raise ValidationError(_('Neispravan email!!!'))    

class AdresarLiceStavkaRegistar(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    korisnikregistar_fk = models.ForeignKey(UserRegistar, on_delete=models.CASCADE)
    datum_kreiranja = models.DateTimeField('datum kreiranja')
    dodatne_informacije = models.CharField(max_length=500)
    telefon = models.CharField(max_length=15,validators=[phone_regex], blank=True)
    prezime = models.CharField(max_length=200)
    adresa = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    ime = models.CharField(max_length=200)
    def clean(self):
        #ovdje treba dodati regex validatore
        if self.ime is None:
            raise ValidationError(_('Lice mora imati ime!!!'))
        if self.prezime is None:
            raise ValidationError(_('Lice mora imati prezime!!!'))            
        if self.telefon is None:
            raise ValidationError(_('Lice mora imati telefon!!!'))

class AdresarFirmaStavkaRegistar(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    korisnikregistar_fk = models.ForeignKey(UserRegistar, on_delete=models.CASCADE)
    datum_kreiranja = models.DateTimeField('datum kreiranja')
    dodatne_informacije = models.CharField(max_length=500)
    telefon = models.CharField(max_length=15,validators=[phone_regex])
    adresa = models.CharField(max_length=200)
    naziv = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    def clean(self):
        #ovdje treba dodati regex validatore
        if self.naziv is None:
            raise ValidationError(_('Firma mora imati naziv!!!'))
        if self.email is None:
            raise ValidationError(_('Firma mora imati email!!!'))            
        if self.telefon is None:
            raise ValidationError(_('Firma mora imati telefon!!!'))
        if self.email is not None and ValidateEmail(self.email):
            raise ValidationError(_('Neispravan email!!!'))    
