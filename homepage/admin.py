from django.contrib import admin

# Register your models here.
from .models import User, Label, Status, Task, TaskLabels
# Register your models here.


admin.site.register(User)
admin.site.register(Label)
admin.site.register(Status)
admin.site.register(TaskLabels)
admin.site.register(Task)
