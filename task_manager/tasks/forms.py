import datetime
from django import forms
from .models import Task
from django.utils.translation import gettext_lazy as _


class CreateStatusForm(forms.ModelForm):
    name = forms.CharField(max_length=150, required=True, label=_("Name"))

    class Meta:
        model = Task
        fields = ('name', 'body', 'status', 'executor',)
