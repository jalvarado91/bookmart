from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.urlresolvers import reverse
from addresses.models import Address
from addresses.forms import AddressForm


@login_required
def addressview(request, user_id, address_id=None):
    address = None
    addresses_list = Address.objects.all().filter(user=user_id)

    if address_id:
        try:
            address = Address.objects.get(pk=address_id)
        except:
            address = None

    if request.method == "POST":
        if address:
            form = AddressForm(request.POST, instance=address)
        else:
            data = {
                'name': request.POST.get('name'),
                'number': request.POST.get('number'),
                'Expdate': request.POST.get('expdate'),
                'Securitycode': request.POST.get('securitycode'),
            }
            form = AddressForm(request.POST, initial=data)

        if form.is_valid():
            newaddress = form.save(commit=False)
            newaddress.user_id = user_id
            newaddress.save()
            return confirmation_page(request, user_id)

    else:  # GET
        if address:
            data = {
                'name': address.name,
                'number': address.number,
                'Expdate': address.expdate,
                'Securitycode': address.securitycode,
            }
            form = AddressForm(instance=address)
            button_text = 'Modify shiping address'
        else:
            form = AddressForm()
            button_text = 'Add new shipping address'

    return render(request, 'addresses/addresses.html', {
        'user_id': user_id,
        'address': address,
        'form': form,
        'addresses_list': addresses_list,
        'button_text': button_text,
    })


def confirmation_page(request, user_id):
    return render(request, 'user_message.html', {
        'page_title':
        'New address confirmation',
        'page_header':
        'Shipping address added succefully',
        'page_message':
        '',
        'url_to_redirect':
        reverse('users:profile', None, [str(user_id)]),
        'returning_page_name':
        'addresses page'
    })
