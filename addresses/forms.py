import re
from django import forms
from django_countries.widgets import CountrySelectWidget

from addresses.models import Address


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['name', 'address1', 'address2', 'city', 'zipcode', 'country']
        widgets = {'country': CountrySelectWidget()}

    def __init__(self, *args, **kwargs):
        super(AddressForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = True
        self.fields['address1'].required = True
        self.fields['city'].required = True
        self.fields['zipcode'].required = True
        self.fields['country'].required = True

        self.fields['name'].widget.attrs[
            'placeholder'] = 'Shipping address familiar name'
        self.fields['address1'].widget.attrs['placeholder'] = 'Address 1'
        self.fields['address2'].widget.attrs['placeholder'] = 'Address 2'
        self.fields['city'].widget.attrs['placeholder'] = 'City'
        self.fields['zipcode'].widget.attrs['placeholder'] = 'Zip Code'
        #self.fields['country'].widget.attrs['layout']

    def clean_zipcode(self):
        zipcode = self.cleaned_data['zipcode']
        self.error_messages = ''
        pattern = re.compile(r'^[0-9]{5}$')

        if not pattern.match(zipcode):
            self.error_messages = 'Wrong zipcode format'
            raise forms.ValidationError(self.error_messages)


class DeleteAddressConfirmation(forms.Form):
    pass