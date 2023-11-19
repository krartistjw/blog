from django.db import models

from users.models import User


class Board(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=False)
    content = models.TextField(blank=False)
