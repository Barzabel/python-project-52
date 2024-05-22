from django.views.generic import (CreateView,
                                  UpdateView,
                                  DeleteView,
                                  DetailView)
from django.views.generic.base import TemplateView
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.mixins import UserLoginMixin, IsAuthorMixin
from .models import Task
from .forms import CreateTaskForm


class TasksView(TemplateView):
    template_name = "tasks/tasks.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks_list'] = Task.objects.all()

        return context

    def get(self, request, *args, **kwargs):
        context = super().get(request, *args, **kwargs)
        messages_ = messages.get_messages(request)
        context['messages'] = messages_
        return context

class TasksDetailView(DetailView):
    template_name = "tasks/tasks_detail.html"
    model = Task


class UpdateTask(UserLoginMixin, SuccessMessageMixin, IsAuthorMixin, UpdateView):
    model = Task
    form_class = CreateTaskForm
    template_name = "form.html"
    error_redirect_url = reverse_lazy('tasks_list')
    is_author_error_message = _("you can't change this task, you are not author")
    success_url = reverse_lazy('tasks_list')
    success_message = _("the task has been successfully changed")
    extra_context = {
        'button_text': _('Change'),
        'title': _('create new status')

    }

class DeleteTask(UserLoginMixin, SuccessMessageMixin, IsAuthorMixin, DeleteView):
    model = Task
    template_name = 'delete.html'
    error_redirect_url = reverse_lazy('tasks_list')
    is_author_error_message = _("you can't delete this task, you are not author")
    success_url = reverse_lazy('tasks_list')
    success_message = _("the task has been successfully delete")
    extra_context = {
        'button_text': _('Yes'),
        'question': _('Are you sure that you want to delete this task ?'),
    }


class CreateTask(UserLoginMixin, SuccessMessageMixin, CreateView):
    form_class = CreateTaskForm
    template_name = "form.html"
    success_url = reverse_lazy('tasks_list')
    success_message = _("the new task has been successfully created")
    extra_context = {
        'button_text': _('Yes'),
        'title': _('create new task')

    }
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.instance.author = self.request.user
        return super().form_valid(form)