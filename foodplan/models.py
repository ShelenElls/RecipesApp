from tkinter import CASCADE
from django.conf import settings
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


USER_MODEL = settings.AUTH_USER_MODEL


class MealPlan(models.Model):
    name = models.CharField(max_length=120)
    date = models.DateTimeField()
    owner = models.ForeignKey(
        USER_MODEL,
        related_name="mealplan",
        on_delete=models.CASCADE,
        null=True,
    )
    recipes = models.ManyToManyField("recipes.Recipe", related_name="recipe")

    def __str__(self):
        return str(self.name) + " by " + str(self.owner)


# class Recipes(models.Model):
#     name = models.CharField()
#     recipes = (models.ManyToManyField("recipes.Foodplan"),)


# class Date(models.Model):
#     created = models.DateTimeField(null=True)


# class Owner(models.Model):
#     author = models.ForeignKey(
#         USER_MODEL,
#         related_name="foodplan",
#         on_delete=models.CASCADE,
#         null=True,
#     )
