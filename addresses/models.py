from __future__ import unicode_literals
from django.db import models
from users.models import Profile


class Address(models.Model):
    name = models.CharField(max_length=100, blank=False)
    address1 = models.CharField('Address line 1', max_length=100, blank=False)
    address2 = models.CharField(
        'Address line 2', max_length=100, blank=True, null=False)
    zipcode = models.CharField('Zip / Postal code', max_length=12, blank=False)
    city = models.CharField('City', max_length=150, blank=False)
    user = models.OneToOneField(Profile, blank=False, on_delete=models.CASCADE)
