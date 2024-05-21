import datetime
from django import forms
from .models import Task
from django.utils.translation import gettext_lazy as _


class CreateTaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('name', 'body', 'status', 'executor' )
