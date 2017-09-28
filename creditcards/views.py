from creditcards.forms import CreditCardForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def creditcardview(request):
    if request.method == "POST":
        form = CreditCardForm(request, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('users/profile')
    else:
        form = CreditCardForm(request)
    return render(request, 'creditcards/creditcards.html', {"form": form})
