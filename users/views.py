# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import FormView, CreateView

from . import forms


@login_required
def profile(request):
    return render(request, 'users/profile.html')


"""
class PasswordChangeView(LoginRequiredMixin, Passw):
    success_url = reverse_lazy('users:profile')
    template_name = 'users/changepassword.html'
"""


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
