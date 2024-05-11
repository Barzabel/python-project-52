from django.shortcuts import render
from django.views import View
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext_lazy as _
from .models import User, Label, Status, Task, TaskLabels
from django.contrib.auth.views import LoginView
from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from .forms import LoginUserForm, RegisterUserForm

class IndexView(View):
    def get(self, request, *args, **kwargs):
        messages_ = messages.get_messages(request)

        return render(
            request,
            'index.html',
            context={
                'messages': messages_
            }
        )



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



class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/singup.html'
    success_url = reverse_lazy('login')



# create users
# login
# get all users
