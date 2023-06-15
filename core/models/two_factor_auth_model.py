from django.db import models
import random
import string
from django.contrib.auth import get_user_model
from datetime import timedelta, datetime
from django.conf import settings
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

User = get_user_model()


def id_generator(size=6, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class AuthCode(models.Model):
    code = models.CharField(max_length=10,
                            blank=False, null=False)
    created_at = models.DateField(auto_now_add=True, blank=False, null=False)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=False, null=False)
    is_used = models.BooleanField(default=False, null=False, blank=False)
    expiration = models.DateTimeField(
        default=datetime.now() + timedelta(hours=2))

    def __str__(self):
        return self.code

    def send_two_factor_email(self):
        subject = 'Otp for signin'
        html_message = render_to_string(
            'mail_templates/otp.html', {'user': self.user, 'code': self.code})
        plain_message = strip_tags(html_message)
        email_from = settings.EMAIL_HOST_USER
        email = EmailMultiAlternatives(
            subject, plain_message, email_from, [self.user.email])
        email.attach_alternative(html_message, "text/html")
        email.send()

    def can_be_sent(self, code):
        return self.expiration < datetime.now() and self.code == code

    def is_expired(self):
        return self.expiration < datetime.now()

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = id_generator()
            while AuthCode.objects.filter(
                    code=self.code).exists():
                self.code = id_generator()
        super(AuthCode, self).save()
