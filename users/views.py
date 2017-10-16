# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import logout, update_session_auth_hash, get_user
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import FormView, CreateView
from users.forms import UserProfileForm, SignUpForm, ProfileForm
from users.models import Profile, User
from django.forms.models import inlineformset_factory
from django.http import Http404
from . import forms


@login_required
def profile(request, pk):
    user = User.objects.get(pk=pk)
    user_form = UserProfileForm(instance=user)

    ProfileFormset = inlineformset_factory(
        User, Profile, fields=('nick_name', ), can_delete=False)
    profile_formset = ProfileFormset(instance=user)

    if request.method == 'POST':
        user_form = UserProfileForm(request.POST, instance=user)
        profile_formset = ProfileFormset(request.POST, instance=user)

        if user_form.is_valid():
            current_user = user_form.save(commit=False)
            profile_formset = ProfileFormset(
                request.POST, instance=current_user)
            current_user.save()

            if profile_formset.is_valid():
                current_user.save()
                profile_formset.save()
                return HttpResponseRedirect('book/index1.html')

            return HttpResponseRedirect(reverse('home'))

        raise Http404('Error validating forms')

    return render(request, 'users/profile.html',
                  {'pk': pk,
                   'form': user_form,
                   'formset': profile_formset})


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


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('users:profile')
