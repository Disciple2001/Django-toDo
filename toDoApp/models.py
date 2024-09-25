from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Task(models.Model):
    TASK_STATUS_CHOICES = (
        (1, 'In Progress'),
        (2, 'Completed'),
    )

    name = models.CharField(max_length=124)
    description = models.TextField(max_length=1024)
    status = models.IntegerField(choices=TASK_STATUS_CHOICES, default=1)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.name
