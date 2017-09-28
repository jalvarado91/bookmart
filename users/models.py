# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse
from django.db import models


class User(models.Model):
    first_name = models.CharField('first name', max_length=30, blank=True)
    last_name = models.CharField('Last name', max_length=30, blank=True)
    email = models.EmailField(max_length=70, unique=True)
    nick_name = models.CharField('Nick name', max_length=30, blank=True)
    user_name = models.CharField('User name', max_length=30, blank=True)
