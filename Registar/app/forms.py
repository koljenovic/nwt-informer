from registration.forms import RegistrationForm
from captcha.fields import CaptchaField

class RegistrationCaptcha(RegistrationForm):
    captcha = CaptchaField()
