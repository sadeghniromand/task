from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.views.generic import FormView, TemplateView, CreateView, ListView
from django.views.generic.edit import ModelFormMixin
from django.urls import reverse
from . import forms


class CreateUserView(CreateView):
    form_class = forms.CreateUserForm
    template_name = 'accounts/register.html'

    def get_success_url(self):
        return reverse('product:home')


class UserLoginView(LoginView):
    template_name = 'accounts/login.html'

    def get_success_url(self):
        return reverse('product:home')


class UserLogoutView(LogoutView):
    def get_next_page(self):
        return reverse('product:home')
