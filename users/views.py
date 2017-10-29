# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.forms.models import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import FormView, CreateView
from users.forms import UserProfileForm, SignUpForm
from users.models import Profile, User
from bookmart.utils import rendermessage, render_access_denied_message
from . import forms


@login_required
def profile(request, user_id):

    try:
        user = User.objects.get(pk=user_id)
        prfl = Profile.objects.get(pk=user_id)
        ProfileFormset = inlineformset_factory(
            User, Profile, fields=('nick_name', ), can_delete=False)
    except:
        return render_access_denied_message(request)

    if request.user.is_authenticated() and request.user.id == user.id:
        if request.method == 'POST':
            user_form = UserProfileForm(instance=user, data=request.POST)
            if user_form.is_valid():
                profile_formset = ProfileFormset(request.POST, instance=prfl)
                #assert False, user
                if profile_formset.is_valid():
                    #assert False, user_form  # at this point both form are valid
                    current_user = user_form.save()
                    #assert False, current_user
                    #saves a new user with empty username
                    #assert False, current_user
                    #profile_formset.user_id = user_id
                    profile_formset.save(request.POST.get('nick_name'))
                    return confirmation_page(request, user_id)

            return render_access_denied_message(request)

        else:
            user_form = UserProfileForm(instance=user)
            profile_formset = ProfileFormset(instance=user)

        return render(request, 'users/profile.html', {
            'user_id': request.user.id,
            'form': user_form,
            'formset': profile_formset,
        })
    else:
        render_access_denied_message(request)


def confirmation_page(request, user_id):
    return rendermessage(request, 'Profile', 'Profile updated succefully', '',
                         reverse('users:profile', args=[str(user_id)]),
                         'profile page')


@login_required
def changepassword(request, user_id):
    form = PasswordChangeForm(user=request.user)
    if request.method == 'POST':
        if "Cancel" in request.POST:
            return reverse('users:profile', args=[str(user_id)]),
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return rendermessage(request, 'Password Confirmation',
                                 'Password changed succefully', '',
                                 reverse('users:profile',
                                         args=[str(user_id)]), 'profile')

    return render(
        request,
        'users/changepassword.html',
        {'form': form,
         'user_name': User.objects.get(pk=user_id)})


class LogoutView(LoginRequiredMixin, FormView):
    form_class = forms.LogoutForm
    template_name = 'users/logout.html'

    def form_valid(self, form):
        logout(self.request)
        return HttpResponseRedirect(reverse('home'))


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'users/signup.html'
    success_url = '/users/login'
