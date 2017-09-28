from django import forms
from .models import CreditCard


class CreditCardForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreditCardForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = True
        self.fields['name'].help_text = 'A familiar name'
        self.fields['number'].requiured = True
        self.fields['expdate'].requiured = True
        self.fields['securitycode'].requiured = True

    class Meta:
        model = CreditCard
        fields = ['name', 'number', 'expdate', 'securitycode']
