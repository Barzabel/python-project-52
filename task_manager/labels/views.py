from django.views.generic import (CreateView,
                                  UpdateView,
                                  DeleteView,
                                  DetailView)
from django.views.generic.base import TemplateView
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.mixins import UserLoginMixin
from task_manager.tasks.models import Task
from .models import Label
from .forms import CreateLabelForm


class LabelsView(TemplateView):
    template_name = "labels/labels.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['labels_list'] = Label.objects.all()

        return context

    def get(self, request, *args, **kwargs):
        context = super().get(request, *args, **kwargs)
        messages_ = messages.get_messages(request)
        context['messages'] = messages_
        return context


class UpdateLabel(UserLoginMixin, SuccessMessageMixin, UpdateView):
    model = Label
    form_class = CreateLabelForm
    template_name = "form.html"
    error_redirect_url = reverse_lazy('labels_list')
    success_url = reverse_lazy('labels_list')
    success_message = _("the lable has been successfully changed")
    extra_context = {
        'button_text': _('Change'),
        'title': _('change label')

    }

class DeleteLabel(UserLoginMixin, SuccessMessageMixin, DeleteView):
    model = Label
    template_name = 'delete.html'
    error_redirect_url = reverse_lazy('labels_list')
    is_author_error_message = _("you can't delete this task, you are not author")
    success_url = reverse_lazy('labels_list')
    success_message = _("the task has been successfully delete")
    extra_context = {
        'button_text': _('Yes'),
        'question': _('Are you sure that you want to delete this lable?'),
    }

    def post(self, request, *args, **kwargs):
        label_id = kwargs['pk']
        tasks_with_label = Task.objects.filter(labels=label_id)

        if tasks_with_label:
            messages.error(
                self.request,
                _('It is not possible to delete a label '
                  'because it is in use')
            )
            return redirect('labels_list')
        return super().post(request, *args, **kwargs)




class CreateLabel(UserLoginMixin, SuccessMessageMixin, CreateView):
    form_class = CreateLabelForm
    template_name = "form.html"
    success_url = reverse_lazy('labels_list')
    success_message = _("the new lable has been successfully created")
    extra_context = {
        'button_text': _('Yes'),
        'title': _('create new label')

    }
