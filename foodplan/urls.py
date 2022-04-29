from django.urls import path

from foodplan.views import (
    MealplanCreateView,
    MealplanDeleteView,
    MealplanUpdateView,
    MealplanDetailView,
    MealplanListView,
)

urlpatterns = [
    path("", MealplanListView.as_view(), name="foodplan_list"),
    path("<int:pk>/", MealplanDetailView.as_view(), name="foodplan_detail"),
    path(
        "<int:pk>/delete/", MealplanDeleteView.as_view(), name="foodplan_delete"
    ),
    path("new/", MealplanCreateView.as_view(), name="foodplan_new"),
    path("<int:pk>/edit/", MealplanUpdateView.as_view(), name="foodplan_edit"),
]
