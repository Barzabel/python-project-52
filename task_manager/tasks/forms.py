from django import forms
from .models import Task
from django.utils.translation import gettext_lazy as _


class CreateTaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('name', 'description', 'status', 'executor', 'labels')
        labels = {
            'name': _('name'),
            'description': _('description'),
            'status': _('status'),
            'executor': _('executor'),
            'labels': _('labels')
        }
