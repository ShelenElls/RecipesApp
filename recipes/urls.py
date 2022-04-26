from django.urls import path

from recipes.views import (
    RecipeListView,
    RecipeCreateView,
    RecipeUpdateView,
    RecipeDeleteView,
    log_rating,
    RecipeDetailView,
)


urlpatterns = [
    path("", RecipeListView.as_view(), name="recipes_list"),
    path("<int:pk>/", RecipeDetailView.as_view(), name="recipe_detail"),
    path("new/", RecipeCreateView.as_view(), name="recipe_new"),
    path("<int:pk>/edit/", RecipeUpdateView.as_view(), name="recipe_edit"),
    path("<int:pk>/delete", RecipeDeleteView.as_view(), name="recipe_delete"),
    path("<int:recipe_id>/ratings/", log_rating, name="recipe_rating"),
]
