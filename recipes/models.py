from django.db import models
from django.forms import DateTimeField

# Create your models here.


class Recipe(models.Model):
    name = models.CharField(max_length=125)
    author = models.CharField(max_length=100)
    description = models.TextField()
    image = models.URLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author


class Measure(models.Model):
    name = models.CharField(max_length=30, unique=True)
    abreviation = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.author


class FoodItem(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.author


class Ingredient(models.Model):
    amount = models.FloatField()
    recipe = models.ForeignKey(
        "Recipe", related_name="ingredients", on_delete=models.CASCADE
    )
    measure = models.ForeignKey("Measure", on_delete=models.PROTECT)
    food = models.ForeignKey("FoodItem", on_delete=models.PROTECT)

    def __str__(self):
        return self.author


class Step(models.Model):
    recipe = models.ForeignKey(
        "Recipe", related_name="Steps", on_delete=models.CASCADE
    )
    order = models.PositiveSmallIntegerField(())
    directions = models.CharField(max_length=300)

    food_items = models.ManyToManyField("FoodItem", null=True, blank=True)

    def __str__(self):
        return self.author
