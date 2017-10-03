from creditcards.forms import CreditCardForm
from creditcards.models import CreditCard
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView


@login_required
def creditcardview(request):
    if request.method == "POST":
        form = CreditCardForm(request, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('users/profile')
    else:
        form = CreditCardForm(request)
    return render(request, 'creditcards/creditcards.html', {'form': form})


class CreditCardDetailView(LoginRequiredMixin, DetailView):
    template_name = 'creditcards/creditcards_detail.html'
    model = CreditCard


class CreditCardListView(LoginRequiredMixin, ListView):
    template_name = 'creditcards/creditcards_list.html'
    model = CreditCard
