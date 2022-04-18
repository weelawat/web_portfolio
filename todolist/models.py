from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todolist(models.Model):
    content = models.TextField(max_length=200)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.content