from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from foodplan.models import MealPlan
from django.shortcuts import redirect


class MealplanListView(LoginRequiredMixin, ListView):
    model = MealPlan
    template_name = "foodplan/mealplan_list.html"
    paginate = 3

    def get_queryset(self):
        return MealPlan.objects.filter(owner=self.request.user)

    def __str__(self):
        return str(self.name)


class MealplanDetailView(LoginRequiredMixin, DetailView):
    model = MealPlan
    template_name = "foodplan/detail.html"

    def get_queryset(self, **kwargs):
        return MealPlan.objects.filter(owner=self.request.user)

    def __str__(self):
        return str(self.name)


class MealplanCreateView(LoginRequiredMixin, CreateView):
    model = MealPlan
    template_name = "foodplan/new.html"
    fields = [
        "name",
        "date",
        "recipes",
    ]
    # success_url = reverse_lazy("recipes_list")

    def form_valid(self, form):
        plan = form.save(commit=False)
        plan.owner = self.request.user
        plan.save()
        form.save_m2m
        return redirect("foodplan_list")

    def __str__(self):
        return str(self.name)


class MealplanUpdateView(LoginRequiredMixin, UpdateView):
    model = MealPlan
    template_name = "foodplan/edit.html"
    fields = [
        "name",
        "recipes",
        "date",
    ]

    def get_queryset(self):
        return MealPlan.objects.filter(owner=self.request.user)

    def get_success_url(self) -> str:
        return reverse_lazy("foodplan_detail", args=[self.object.id])

    def __str__(self):
        return str(self.name)


class MealplanDeleteView(LoginRequiredMixin, DeleteView):
    model = MealPlan
    template_name = "foodplan/delete.html"
    success_url = reverse_lazy("foodplan_list")

    def get_queryset(self):
        return MealPlan.objects.filter(owner=self.request.user)

    def __str__(self):
        return str(self.name)
