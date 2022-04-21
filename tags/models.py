from django.db import models
from recipes.models import Recipe


class Tag(models.Model):
    name = models.CharField(max_length=20)
    recipes = models.ManyToManyField(Recipe, related_name=("tags"))

    def __str__(self):
        return self.name
