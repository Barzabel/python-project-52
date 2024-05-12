from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext as _


class UserLoginMixin(LoginRequiredMixin):
    auth_messages = _('You are not logged in! You need to log in.')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, self.auth_messages)
            return redirect(reverse_lazy('login'))

        return super().dispatch(request, *args, **kwargs)


