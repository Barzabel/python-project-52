from django.contrib import admin
from .models import Label, Task, TaskLabels


admin.site.register(Label)
admin.site.register(TaskLabels)
admin.site.register(Task)
