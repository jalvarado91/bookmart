from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from addresses.models import Address


class AddressDetailView(LoginRequiredMixin, DetailView):
    template_name = 'addresses/addresses_detail.html'
    model = Address


class AddressesListView(LoginRequiredMixin, ListView):
    template_name = 'addresses/adresses_list.html'
    model = Address