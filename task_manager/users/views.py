from django.shortcuts import render
from django.views import View
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext_lazy as _
from .models import User
from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from django.views.generic.edit import DeleteView, UpdateView
from .forms import UserForm
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.mixins import UserLoginMixin, AuthorizationMixin


class UpdateUser(UserLoginMixin,AuthorizationMixin, SuccessMessageMixin, UpdateView):
    model = User
    success_url = reverse_lazy('users')
    success_message = _("the user has been successfully changed")
    fields = ['username', 'email', 'first_name', 'last_name']
    permission_denied_message = _("You can't change this profile, this is not you")
    permission_denied_url = reverse_lazy('users')
    success_url = reverse_lazy("home")
    template_name_suffix = "_update_form"
    extra_context = {
        'button_text': _('Yes'),
    }

class DeleteUser(UserLoginMixin, AuthorizationMixin, SuccessMessageMixin, DeleteView):
    model = User
    success_message = _("the user has been deleted")
    template_name = 'delete.html'
    permission_denied_message = _("You can't change this profile, this is not you")
    permission_denied_url = reverse_lazy('users')
    success_url = reverse_lazy('users')
    extra_context = {
        'button_text': _('Yes'),
        'question': _('Are you sure that you want to delete this user?')
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


class RegisterUser(SuccessMessageMixin, CreateView):
    form_class = UserForm
    success_url = reverse_lazy('users')
    success_message = _("the new user has been successfully created")
    template_name = 'form.html'
    extra_context = {
        'button_text': _('sing up'),
        'title': _('sing up user')
    }
