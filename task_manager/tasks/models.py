from django.db import models
from task_manager.users.models import User
from task_manager.status.models import Status
from task_manager.labels.models import Label



class Task(models.Model):

    name = models.CharField(max_length=150, blank=False, unique=True)
    body = models.TextField(max_length=1000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, related_name='author', on_delete=models.CASCADE)
    status = models.ForeignKey(Status, related_name='status', on_delete=models.CASCADE)
    executor = models.ForeignKey(User, related_name='executor', on_delete=models.CASCADE)
    labels = models.ManyToManyField(
                                Label, 
                                through='TaskLabels', 
                                through_fields=('task', 'label'),
                                blank=True,
                                related_name='labels',
                            )

    def __str__(self):
        return self.name


class TaskLabels(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.PROTECT)
