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
from django_filters import FilterSet, ModelChoiceFilter, BooleanFilter
from django_filters.views import FilterView
from task_manager.labels.models import Label
from .models import Task
from .forms import CreateTaskForm
from django import forms


class TaskFilter(FilterSet):

    labels = ModelChoiceFilter(queryset=Label.objects.all(), label=_('Label'))

    own_tasks = BooleanFilter(label=_('Only own tasks'),
                              widget=forms.CheckboxInput,
                              method='queryset_own_tasks',)

    def queryset_own_tasks(self, queryset, name, value):
        if value:
            user = self.request.user
            return queryset.filter(author=user)
        return queryset

    class Meta:
        model = Task
        fields = (
            'status',
            'executor',
        )
        labels = {
            'status': _('status'),
            'executor': _('executor'),

        }



class TasksView(UserLoginMixin, FilterView):
    model = Task
    filterset_class = TaskFilter
    template_name = 'tasks/tasks.html'
    context_object_name = 'tasks'
    extra_context = {
        'title': _('Tasks'),
        'button_text': _('Show'),
    }





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
        'button_text': _('Yes, delete'),
        'question': _('Are you sure that you want to delete this task ?'),
    }


class CreateTask(UserLoginMixin, SuccessMessageMixin, CreateView):
    form_class = CreateTaskForm
    template_name = "form.html"
    success_url = reverse_lazy('tasks_list')
    success_message = _("the new task has been successfully created")
    extra_context = {
        'button_text': _('Create'),
        'title': _('create new task')

    }
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.instance.author = self.request.user
        return super().form_valid(form)