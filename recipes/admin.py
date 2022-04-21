from django.contrib import admin
from recipes.models import Ingredient, Measure, FoodItem, Step, Recipe

# Register your models here.
class RecipeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Recipe, RecipeAdmin)


class MeasureAdmin(admin.ModelAdmin):
    pass


admin.site.register(Measure, MeasureAdmin)


class FoodItemAdmin(admin.ModelAdmin):
    pass


admin.site.register(FoodItem, FoodItemAdmin)


class IngredientAdmin(admin.ModelAdmin):
    pass


admin.site.register(Ingredient, IngredientAdmin)


class StepAdmin(admin.ModelAdmin):
    pass


admin.site.register(Step, StepAdmin)
