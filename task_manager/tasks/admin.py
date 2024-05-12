from django.contrib import admin
from .models import Label, Status, Task, TaskLabels


admin.site.register(Label)
admin.site.register(Status)
admin.site.register(TaskLabels)
admin.site.register(Task)
