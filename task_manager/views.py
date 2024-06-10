from django.shortcuts import render
from django.views import View
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


class LoginUser(SuccessMessageMixin, LoginView):
    '''Form log in User'''
    template_name = 'form.html'
    success_message = _('You are logged in !')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'button_text': _('Enter')})
        return context


class LogoutUser(LogoutView):
    '''Form Logout User'''

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, _('You are logged out'))
        return super().dispatch(request, *args, **kwargs)


class IndexView(View):
    def get(self, request, *args, **kwargs):
        messages_ = messages.get_messages(request)

        return render(
            request,
            'index.html',
            context={
                'messages': messages_,
            }
        )
