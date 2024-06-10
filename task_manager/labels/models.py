from django.db import models


class Label(models.Model):
    name = models.CharField(max_length=150, unique=True, blank=False,)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
