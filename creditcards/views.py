from creditcards.forms import CreditCardForm
from creditcards.models import CreditCard
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse


@login_required
def creditcardview(request, user_id, creditcard_id=None):
    creditcard = None
    creditcards_list = CreditCard.objects.all().filter(user=user_id)

    if creditcard_id:
        try:
            creditcard = CreditCard.objects.get(pk=creditcard_id)
        except:
            creditcard = None

    if request.method == "POST":
        if creditcard:
            form = CreditCardForm(request.POST, instance=creditcard)
        else:
            data = {
                'name': request.POST.get('name'),
                'number': request.POST.get('number'),
                'Expdate': request.POST.get('expdate'),
                'Securitycode': request.POST.get('securitycode'),
            }
            form = CreditCardForm(request.POST, initial=data)

        if form.is_valid():
            newcreditcard = form.save(commit=False)
            newcreditcard.user_id = user_id
            newcreditcard.save()
            return confirmation_page(request, user_id)

    else:  # GET
        #assert False, creditcard.id
        if creditcard:
            data = {
                'name': creditcard.name,
                'number': creditcard.number,
                'Expdate': creditcard.expdate,
                'Securitycode': creditcard.securitycode,
            }
            form = CreditCardForm(instance=creditcard)
            button_text = 'Modify credit card'
        else:
            form = CreditCardForm()
            button_text = 'Add credit card'

    return render(request, 'creditcards/creditcards.html', {
        'user_id': user_id,
        'creditcard': creditcard,
        'form': form,
        'creditcards_list': creditcards_list,
        'button_text': button_text,
    })


def confirmation_page(request, user_id):
    return render(request, 'user_message.html', {
        'page_title':
        'Credit card confirmation',
        'page_header':
        'Credit card added succefully',
        'page_message':
        '',
        'url_to_redirect':
        reverse('users:profile', None, [str(user_id)]),
        'returning_page_name':
        'creditcards page'
    })


"""
class CreditCardDetailView(LoginRequiredMixin, DetailView):
    template_name = 'creditcards/creditcards_detail.html'
    model = CreditCard


class CreditCardListView(LoginRequiredMixin, ListView):
    template_name = 'creditcards/creditcards_list.html'
    model = CreditCard
"""