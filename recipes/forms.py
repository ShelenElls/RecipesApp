from django import forms
from recipes.models import Rating
from recipes.models import Recipe
from django.conf import settings


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ["value"]


USER_MODEL = settings.AUTH_USER_MODEL
