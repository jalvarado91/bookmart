# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse
from django.db import models


class User(models.Model):
    first_name = models.CharField('First name', max_length=30, blank=False, null = True)
    last_name = models.CharField('Last name', max_length=30, blank=False, null = True)
    email = models.EmailField(max_length=70, unique=True, null = True)
    nick_name = models.CharField('Nick name', max_length=30, blank=False)
    user = models.CharField('Username', max_length=30, blank=False, null = True)
