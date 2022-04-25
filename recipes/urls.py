from django.urls import path

from recipes.views import (
    RecipeListView,
    create_recipe,
    change_recipe,
    log_rating,
    RecipeDetailView,
    RecipeListView,
)


urlpatterns = [
    path("", RecipeListView.as_view(), name="recipes_list"),
    path("<int:pk>/", RecipeDetailView.as_view(), name="recipe_detail"),
    path("new/", create_recipe, name="recipe_new"),
    path("edit/", change_recipe, name="recipe_edit"),
    path("<int:recipe_id>/ratings/", log_rating, name="recipe_rating"),
]
