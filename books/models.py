# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ManyToManyField(Author)
    cover_url = models.CharField(max_length=200)
    description = models.TextField()
    genre = models.CharField(max_length=200)
    price = models.FloatField()
    rating = models.IntegerField(blank=True, null=True)
    publisher = models.CharField(max_length=100)
    release_date = models.DateTimeField('publishing date')

    def __str__(self):
        return self.title
