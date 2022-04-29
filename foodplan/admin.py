from django.contrib import admin

from foodplan.models import MealPlan

# Register your models here.


class MealPlanAdmin(admin.ModelAdmin):
    pass


admin.site.register(MealPlan, MealPlanAdmin)
