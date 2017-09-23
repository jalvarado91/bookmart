#carts/models.py
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
#from booksmart.models import books

# Create your models here.
class Cart(models.Model):
    #user = models.ForeignKey(users.User)
    #items = models.ManyToManyField('books.Book')
    item_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.id)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart)
    #item = models.ForeignKey(books.Book)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.item

class SavedItem(models.Model):
    cart = models.ForeignKey(Cart)
    #item = models.ForeignKey(books.Book)

    def __str__(self):
        return self.item
