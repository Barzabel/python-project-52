from django.shortcuts import render
from django.views import View
from django.contrib.auth.views import LoginView
from .forms import LoginUserForm
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


class LoginUser(LoginView):
    form_class = LoginUserForm
    success_message = _('You are logged in !')
    template_name = 'users/login.html'



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