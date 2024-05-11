from django.shortcuts import render
from django.views import View
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from .models import User, Label, Status, Task, TaskLabels
from django.contrib.auth.views import LoginView
from .forms import LoginUserForm

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


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация'}


# create users
# login
# get all users
