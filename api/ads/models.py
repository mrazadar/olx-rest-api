# models.py
from sqlite3 import Date

from django.db import models


class Ad(models.Model):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=255)
    price = models.IntegerField()
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
