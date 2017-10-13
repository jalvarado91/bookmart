from django import forms
from addresses.models import Address
from addresses.models import Address


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['name', 'address1', 'address2', 'city', 'zipcode']

    def __init__(self, request, *args, **kwargs):
        super(AddressForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = True
        self.fields['address1'].required = True
        self.fields['address2'].required = True
        self.fields['city'].required = True
        self.fields['zipcode'].required = True
