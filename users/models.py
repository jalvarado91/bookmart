# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


<<<<<<< HEAD
class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    nick_name = models.CharField('Nick name', max_length=30, null=True)
=======
class User(models.Model):
    first_name = models.CharField('First name', max_length=30, blank=False)
    last_name = models.CharField('Last name', max_length=30, blank=False)
    email = models.EmailField(max_length=70, unique=True)
    nick_name = models.CharField('Nick name', max_length=30, blank=False)
    user = models.CharField('Username', max_length=30, blank=False)
>>>>>>> 160d73146d20e01b820dabba3bc5ad2d700e0470
