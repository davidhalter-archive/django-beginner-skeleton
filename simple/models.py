import re

from django.db import models
from django.forms import ValidationError


class PhoneField(models.CharField):
    def validate(self, number, model_instance):
        if not re.match('^\+?\d+$', number):
            raise ValidationError('Need a valid phone number!')
        return super(PhoneField, self).validate(number, model_instance)


class Bank(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    boss = models.CharField(max_length=200)
    phone = PhoneField(max_length=20, unique=True)
