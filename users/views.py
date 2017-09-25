# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeDoneView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import FormView, CreateView

from . import forms


@login_required
def profile(request):
    return render(request, 'users/profile.html')


@login_required
def resetpassword(request):
    form = PasswordChangeForm(user=request.user)
    success_url = 'users/passwordchanged.html'

    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)

    return render(request, 'users/resetpassword.html', {
        'form': form,
    })


class MyPasswordChangeDoneView(PasswordChangeDoneView):
    form_class = PasswordChangeDoneView
    template_name = 'users/passwordchanged.html'
    success_url = reverse_lazy('users:profile')


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
