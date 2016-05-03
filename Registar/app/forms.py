from registration.forms import RegistrationForm
from captcha.fields import CaptchaField

from djng.forms import NgFormValidationMixin, NgModelForm, NgModelFormMixin, NgFormValidationMixin
from djng.styling.bootstrap3.forms import Bootstrap3FormMixin

class RegistrationCaptcha(Bootstrap3FormMixin, NgModelFormMixin, NgFormValidationMixin, NgModelForm, RegistrationForm):
    captcha = CaptchaField()
