from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=120)
    created_at = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    is_done = models.BooleanField(default=False)
    priority = models.IntegerField(
        choices=[(1, "Low"), (2, "Medium"), (3, "High")],
        default=2,
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Task {self.id}: {self.title}"
