#carts/views.py
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View

# Create your views here.

from carts.models import Cart, CartItem

def CartView(request):
    return render(request, 'cart/cart.html')
