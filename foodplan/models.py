from tkinter import CASCADE
from django.conf import Settings
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


from foodplan.forms import USER_MODEL

USER_MODEL = Settings.AUTH_USER_MODEL


class Mealplan(models.Model):
    name = models.CharField(max_length=125)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Recipes(models.Model):
    name = 

class Da    