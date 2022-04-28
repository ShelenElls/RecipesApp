from django.urls import path

from foodplan.views import (
    FoodplanCreateView,
    FoodplanDeleteView,
    FoodplanUpdateView,
    FoodplanDetailView,
    FoodplanListView,
)

urlpatters = [
    path("", FoodplanDetailView.as_view(), name="meal_list"),
    path("<int:pk>/", FoodplanDetailView.as_view(), name="meal_detail"),
    path("<int:pk>/delete/", FoodplanDeleteView.as_view(), name="meal_delete"),
    path("new/", FoodplanCreateView.asview(), name="meal_new"),
    path("<int:pk>/edit/", FoodplanUpdateView.as_view(), name="meal_edit"),
]
