from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.urlresolvers import reverse
from addresses.models import Address
from addresses.forms import AddressForm
from bookmart.utils import rendermessage


@login_required
def addressview(request, user_id, address_id=None):
    address = None
    addresses_list = Address.objects.all().filter(user=user_id)

    if address_id:
        try:
            address = Address.objects.get(pk=address_id)
            addresses_list = Address.objects.filter(user=user_id).exclude(
                pk=address_id)
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
            return rendermessage(request, 'New address confirmation',
                                 'Shipping address added succefully', '',
                                 reverse('users:addresses', None,
                                         [str(user_id)]), 'addresses page')

    else:  # GET
        if address:
            data = {
                'name': address.name,
                'address1': address.address1,
                'address2': address.address2,
                'city': address.city,
                'zipcode': address.zipcode,
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
