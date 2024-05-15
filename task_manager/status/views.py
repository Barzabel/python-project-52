from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext_lazy as _
from .models import Status


class StatusView(TemplateView):
    template_name = "status/status.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status_list'] = Status.objects.all()

        return context

    def get(self, request, *args, **kwargs):
        context = super().get(request, *args, **kwargs)
        messages_ = messages.get_messages(request)
        context['messages'] = messages_
        return context

class UpdateStatus(TemplateView):
    pass

class DeleteStatus(TemplateView):
    pass