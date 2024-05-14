from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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


class AuthorizationMixin(UserPassesTestMixin):
    permission_denied_message = None
    permission_denied_url = None

    def test_func(self):
        '''Check user'''

        return self.get_object() == self.request.user

    def handle_no_permission(self):
        '''If error permission,
        we handle this error and redirect to denied url'''

        messages.error(self.request, self.permission_denied_message)
        return redirect(self.permission_denied_url)