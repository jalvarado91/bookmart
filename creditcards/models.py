from django.db import models
from users.models import User


class CreditCard(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=16)
    expdate = models.CharField(max_length=4)
    securitycode = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
