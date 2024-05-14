from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.utils.translation import gettext as _
from django.contrib import messages
from django.urls import reverse, reverse_lazy



class UserLoginMixin(LoginRequiredMixin):
    auth_messages = _('You are not logged in! You need to log in.')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, self.auth_messages)
            return redirect(reverse_lazy('login'))

        return super().dispatch(request, *args, **kwargs)


