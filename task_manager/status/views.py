from django.views.generic import CreateView
from django.views.generic.edit import DeleteView, UpdateView
from django.views.generic.base import TemplateView
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.mixins import UserLoginMixin
from .models import Status
from .forms import CreateStatusForm


class StatusView(UserLoginMixin, TemplateView):
    template_name = "status/status.html"
    auth_messages = None
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status_list'] = Status.objects.all()

        return context

    def get(self, request, *args, **kwargs):
        context = super().get(request, *args, **kwargs)
        messages_ = messages.get_messages(request)
        context['messages'] = messages_
        return context

class UpdateStatus(UserLoginMixin, SuccessMessageMixin, UpdateView):
    model = Status
    form_class = CreateStatusForm
    template_name = "form.html"
    success_url = reverse_lazy('status_list')
    success_message = _("the status has been successfully changed")
    extra_context = {
        'button_text': _('Change'),
        'title': _('create new status')

    }

class DeleteStatus(UserLoginMixin, SuccessMessageMixin, DeleteView):
    model = Status
    success_url = reverse_lazy('status_list')
    success_message = _("the status has been deleted")
    extra_context = {
        'button_text': _('Yes'),
    }


class CreateStatus(UserLoginMixin, SuccessMessageMixin, CreateView):
    form_class = CreateStatusForm
    template_name = "form.html"
    success_url = reverse_lazy('status_list')
    success_message = _("the new status has been successfully created")
    extra_context = {
        'button_text': _('Yes'),
        'title': _('create new status')

    }