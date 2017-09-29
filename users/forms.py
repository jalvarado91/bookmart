from django import forms
from .models import User
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import re


class LogoutForm(forms.Form):
    pass


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'nick_name', 'user']

    def __init__(self, request, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.request = request
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True
        self.fields['user'].required = True

    def save(self):
        cleaned_data = self.cleaned_data

    def validate_non_numeric(self, str_exp):
        pattern = re.compile(r"([a-zA-Z]+)")
        if not pattern.match(str_exp):
            raise ValidationError('Email format is incorrect')
        return str_exp

    def clean_first_name(self):
        return self.validate_non_numeric(self.cleaned_data['first_name'])

    def clean_last_name(self):
        return self.validate_non_numeric(self.cleaned_data['last_name'])

    def clean_email(self):
        value = self.cleaned_data['email']
        pattern = re.compile(
            r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
        if not pattern.match(value):
            raise ValidationError('Email format is incorrect')
        return value
