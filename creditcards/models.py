from django.db import models
from users.models import Profile


class CreditCard(models.Model):
    name = models.CharField(max_length=100, blank=False)
    number = models.CharField(max_length=16, blank=False, unique=True)
    expdate = models.CharField(max_length=4, blank=False)
    securitycode = models.IntegerField(blank=False)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=False)
