from django.db import models
from users.models import User


class Label(models.Model):
    name = models.CharField(max_length=150, unique=True, blank=False,)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=150, unique=True, blank=False,)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Task(models.Model):

    name = models.CharField(max_length=150, blank=False, unique=True)
    body = models.TextField(max_length=1000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, related_name='author', on_delete=models.PROTECT)
    status = models.ForeignKey(Status, related_name='status', on_delete=models.PROTECT)
    executor = models.ForeignKey(User, related_name='executor', on_delete=models.PROTECT)
    labels = models.ManyToManyField(Label, through='TaskLabels', through_fields=('task', 'label'), related_name='labels')

    def __str__(self):
        return self.name


class TaskLabels(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.PROTECT)
