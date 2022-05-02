from django import forms
from recipes.models import Rating
from recipes.models import Recipe
from django.conf import settings


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ["value"]

    def __str__(self):
        return str(self.name)


USER_MODEL = settings.AUTH_USER_MODEL
