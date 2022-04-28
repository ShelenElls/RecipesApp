from django import forms
from foodplan.models import Mealplan
from foodplan.views import Views
from django.conf import settings


USER_MODEL = settings.AUTH_USER_MODEL
