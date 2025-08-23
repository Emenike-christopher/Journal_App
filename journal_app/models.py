from django.db import models
from django.contrib.auth.models import User as user

class journal(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(user, on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


