from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Slika)
admin.site.register(Firma)
admin.site.register(Grad)
admin.site.register(Uloga)
admin.site.register(Osoba)
admin.site.register(VrstaKontakta)
admin.site.register(Kontakt)
admin.site.register(Adresar)