from ast import Delete
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from recipes.forms import RatingForm
from django.contrib.auth.mixins import LoginRequiredMixin
from recipes.models import Ingredient, Recipe, Shopping_item, Step
from django.views.decorators.http import require_http_methods
from psycopg2 import IntegrityError


def log_rating(request, recipe_id):
    if request.method == "POST":
        form = RatingForm(request.POST)
        try:
            form.is_valid()
            rating = form.save(commit=True)
            rating.recipe = Recipe.objects.get(pk=recipe_id)
            rating.save()
        except Recipe.DoesNotExist:
            return redirect("recipes_list")
    return redirect("recipe_detail", pk=recipe_id)


class RecipeListView(ListView):
    model = Recipe
    template_name = "recipes/list.html"
    context_object_name = "recipe_list"
    paginate_by = 3

    def __str__(self):
        return str(self.name)


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipes/detail.html"

    def __str__(self):
        return str(self.name)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["rating_form"] = RatingForm()
        foods = []
        for item in self.request.user.shopping_items.all():
            foods.append(item.food_item)
        context["food_in_shopping_list"] = foods
        return context


@require_http_methods(["POST"])
def create_shopping_item(request):
    ingredient_id = request.POST.get("ingredient_id")
    ingredient = Ingredient.objects.get(id=ingredient_id)
    user = request.user
    try:
        Shopping_item.objects.create(
            food_item=ingredient.food,
            user=user,
        )
    except IntegrityError:
        pass
    return redirect("recipe_detail", pk=ingredient.recipe.id)


def delete_all_shopping_items(request):
    Shopping_item.objects.filter(user=request.user).delete()
    return redirect("shopping_item/list")


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = "recipes/new.html"
    fields = [
        "name",
        "image",
        "description",
        "ingredient",
        "servings",
        "steps",
    ]
    success_url = reverse_lazy("recipes_list")

    def __str__(self):
        return str(self.name)

    # def form_valid(self, fsssorm):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)


class RecipeUpdateView(UpdateView):
    model = Recipe
    template_name = "recipes/edit.html"
    fields = ["name", "author", "description", "image"]
    success_url = reverse_lazy("recipes_list")

    def __str__(self):
        return str(self.name)


class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = "recipes/delete.html"
    success_url = reverse_lazy("recipes_list")

    def __str__(self):
        return str(self.name)


class ShoppingItemListView(LoginRequiredMixin, ListView):
    model = Shopping_item
    template_name = "shopping_items/list.html"

    def get_queryset(self):
        return Shopping_item.objects.filter(user=self.request.user)
