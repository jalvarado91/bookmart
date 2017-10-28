from django import forms
from .models import CreditCard
from django.core.exceptions import ValidationError
import re


class CreditCardForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreditCardForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Credit card name'
        self.fields['number'].widget.attrs[
            'placeholder'] = 'Credit card number'
        self.fields['expdate'].widget.attrs['placeholder'] = 'Expiration date'
        self.fields['securitycode'].widget.attrs[
            'placeholder'] = 'Security code'

    class Meta:
        model = CreditCard
        fields = ['name', 'number', 'expdate', 'securitycode']

    def clean_number(self):
        value = self.cleaned_data['number']
        pattern = re.compile(r"[0-9]{16}")
        if not pattern.match(str(value)):
            raise ValidationError('credit card number is incorrect')
        return value

    def clean_expdate(self):
        value = self.cleaned_data['expdate']
        pattern = re.compile(r"^[0-9]{4}")
        if not pattern.match(str(value)):
            raise ValidationError('expiration date is incorrect')
        return value

    def clean_securitycode(self):
        value = self.cleaned_data['securitycode']
        pattern = re.compile(r"^[0-9]{4}")
        if not pattern.match(str(value)):
            raise ValidationError('security code is incorrect')
        return value

    def clean(self):
        super(CreditCardForm, self).clean()
        #name = self.cleaned_data.get('name')
        #number = self.cleaned_data.get('number')
        #expdate = self.cleaned_data.get('expdate')
        #securitycode = self.cleaned_data.get('securitycode')


class DeleteCreditCardConfirmation(forms.Form):
    pass