# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import FormView, CreateView, DetailView
#from crispy_forms.helper import FormHelper

from . import forms
"""
class ProfileView(LoginRequiredMixin, DetailView):
    template_name = 'users/profile.html'

def get_user_profile(request, username):
    user = User.objects.get(username=username)
    return render(request, 'users/user_profile.html', {"user": user})
"""


def profile(request):
    if request.user.is_authenticated:
        return render(request, 'users/profile.html')
    else:
        return HttpResponseRedirect(reverse('home'))


class LogoutView(LoginRequiredMixin, FormView):
    form_class = forms.LogoutForm
    template_name = 'users/logout.html'

    def form_valid(self, form):
        logout(self.request)
        return HttpResponseRedirect(reverse('home'))


class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('users:profile')
