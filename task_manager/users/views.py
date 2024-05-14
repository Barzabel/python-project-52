from django.shortcuts import render
from django.views import View
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext_lazy as _
from .models import User
from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from django.views.generic.edit import DeleteView, UpdateView
from .forms import LoginUserForm, RegisterUserForm
from .mixins import UserLoginMixin, AuthorizationMixin


class UpdateUser(UserLoginMixin,AuthorizationMixin, UpdateView):
    model = User
    fields = ['username', 'email', 'first_name', 'last_name']
    permission_denied_message = _("You can't change this profile, this is not you")
    permission_denied_url = reverse_lazy('users')
    success_url = reverse_lazy("home")
    template_name_suffix = "_update_form"
    extra_context = {
        'button_text': _('Yes'),
    }




class DeleteUser(UserLoginMixin, AuthorizationMixin, DeleteView):
    model = User
    success_url = reverse_lazy("home")

    permission_denied_message = _("You can't change this profile, this is not you")
    permission_denied_url = reverse_lazy('users')
    success_message = _('User deleted')
    success_url = reverse_lazy('users')
    extra_context = {
        'button_text': _('Yes'),
    }



class UseersView(TemplateView):
    template_name = "users/users.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users_list'] = User.objects.all()

        return context

    def get(self, request, *args, **kwargs):
        context = super().get(request, *args, **kwargs)
        messages_ = messages.get_messages(request)
        context['messages'] = messages_
        return context


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/singup.html'
    success_url = reverse_lazy('login')
    extra_context = {
        'button_text': _('sing up'),
    }
