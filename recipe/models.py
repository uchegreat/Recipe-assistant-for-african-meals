"""
from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    ingredients = models.TextField()
    instructions = models.TextField()
    image = models.URLField(blank=True, null=True)  # ✅ Store image URL

    def __str__(self):
        return self.name
"""

