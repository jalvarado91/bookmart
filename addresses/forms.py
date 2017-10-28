from django import forms
from addresses.models import Address
from addresses.models import Address


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['name', 'address1', 'address2', 'city', 'zipcode']

    def __init__(self, *args, **kwargs):
        super(AddressForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = True
        self.fields['address1'].required = True
        self.fields['city'].required = True
        self.fields['zipcode'].required = True

        self.fields['name'].widget.attrs[
            'placeholder'] = 'Shipping address familiar name'
        self.fields['address1'].widget.attrs['placeholder'] = 'Address 1'
        self.fields['address2'].widget.attrs['placeholder'] = 'Address 2'
        self.fields['city'].widget.attrs['placeholder'] = 'City'
        self.fields['zipcode'].widget.attrs['placeholder'] = 'Zip Code'
