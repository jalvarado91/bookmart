# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import FormView, CreateView
from .forms import UserProfileForm

from . import forms


#from .forms import ProfileForm
@login_required
def profile(request):
    form = UserProfileForm(request)
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return HttpResponseRedirect('/thanks/')
    else:
        form = UserProfileForm(request)
    return render(request, 'users/profile.html', {'form': form})


@login_required
def changepassword(request):
    form = PasswordChangeForm(user=request.user)
    success_url = reverse_lazy('users:profile')
    if request.method == 'POST':
        if "Cancel" in request.POST:
            return HttpResponseRedirect(success_url)
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return render(request, 'users/changepassworddone.html')

    return render(request, 'users/changepassword.html', {
        'form': form,
    })


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
