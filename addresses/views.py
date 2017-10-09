from addresses.forms import AddressForm
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from addresses.models import Address
from django.contrib.auth.decorators import login_required


class AddressDetailView(LoginRequiredMixin, DetailView):
    template_name = 'addresses/addresses_detail.html'
    model = Address


class AddressesListView(LoginRequiredMixin, ListView):
    template_name = 'addresses/adresses_list.html'
    model = Address


@login_required
def addressview(request):
    if request.method == "POST":
        form = AddressForm(request, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('users/profile')
    else:
        form = AddressForm(request)
    return render(request, 'addresses/addresses_detail.html', {'form': form})