import datetime
from django import forms
from .models import Label
from django.utils.translation import gettext_lazy as _


class CreateLabelForm(forms.ModelForm):

    class Meta:
        model = Label
        fields = ('name', )