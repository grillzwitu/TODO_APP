from datetime import date
from operator import mod
from unicodedata import name
from django.db import models

# Create your models here.
class Task(models.Model):
    """Creating The task Model"""

    name = models.CharField(max_length=400)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        """Changes __str__ to self.name"""
        return self.name
