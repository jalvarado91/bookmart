#carts/models.py
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
import books
import users


# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(users.models.Profile)
    item_count = models.PositiveIntegerField(default=0)
    order_date = models.DateField(null=True)

    def __str__(self):
        return str(self.id)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart)
    item = models.ForeignKey(books.models.Book)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.item


class SavedItem(models.Model):
    cart = models.ForeignKey(Cart)
    item = models.ForeignKey(books.models.Book)

    def __str__(self):
        return self.item
