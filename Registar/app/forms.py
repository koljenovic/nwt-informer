from registration.forms import RegistrationForm
from captcha.fields import CaptchaField
from app.models import *
from djng.forms import NgFormValidationMixin, NgModelForm, NgModelFormMixin, NgFormValidationMixin, NgForm
from djng.styling.bootstrap3.forms import Bootstrap3FormMixin


# Uloga, Grad, Firma, Osoba, VrstaKontakta, Kontakt, Adresar

class RegistrationCaptcha(Bootstrap3FormMixin, NgModelFormMixin, NgFormValidationMixin, NgModelForm, RegistrationForm):
    scope_prefix = 'registration_data'
    form_name = 'registration_form'

    captcha = CaptchaField()


class FirmaForm(Bootstrap3FormMixin, NgModelFormMixin, NgFormValidationMixin, NgModelForm):
    class Meta:
        model = Firma
        exclude = ['logo', 'slika_zaglavlje']

    scope_prefix = 'form_data'
    form_name = 'app_form'
    form_header = 'Firma profil'


class OsobaForm(Bootstrap3FormMixin, NgModelFormMixin, NgFormValidationMixin, NgModelForm):
    class Meta:
        model = Osoba
        exclude = ['datum_registracije', 'slika']

    scope_prefix = 'form_data'
    form_name = 'app_form'
    form_header = 'Osoba profil'
