# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse, reverse_lazy
from django.forms.models import inlineformset_factory
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import FormView, CreateView
from users.forms import UserProfileForm, SignUpForm
from users.models import Profile, User
from . import forms


@login_required
def profile(request, user_id):

    user = User.objects.get(pk=user_id)
    profile = Profile.objects.get(pk=user_id)
    ProfileFormset = inlineformset_factory(
        User, Profile, fields=('nick_name', ), can_delete=False)

    if request.user.is_authenticated() and request.user.id == user.id:

        if request.method == 'POST':
            user_form = UserProfileForm(request.POST, instance=user)

            if user_form.is_valid():
                current_user = user_form.save(commit=False)
                profile_formset = ProfileFormset(
                    request.POST, instance=profile)

                if profile_formset.is_valid():
                    current_user.save()
                    profile_formset.save()
                    return confirmation_page(request, user_id)

            raise Http404('Error validating forms')  # not valid

        else:
            user_form = UserProfileForm(instance=user)
            profile_formset = ProfileFormset(instance=user)

        return render(request, 'users/profile.html', {
            'user_id': request.user.id,
            'form': user_form,
            'formset': profile_formset,
        })
    else:
        raise Http404('Access denied')


def confirmation_page(request, user_id):
    return render(request, 'user_message.html', {
        'page_title':
        'Profile',
        'page_header':
        'Profile updated succefully',
        'page_message':
        '',
        'url_to_redirect':
        reverse('users:profile', None, [str(user_id)]),
        'returning_page_name':
        'profile page'
    })


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
            return render(request, 'user_message.html', {
                'page_title':
                'Password Confirmation',
                'page_header':
                'Password changed succefully',
                'page_message':
                '',
                'url_to_redirect':
                reverse('users:profile', None, [str(user_id)]),
                'returning_page_name':
                'profile'
            })

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
    success_url = '/users/login'
