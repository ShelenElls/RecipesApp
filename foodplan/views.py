from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from foodplan.models import MealPlan


class MealplanListView(LoginRequiredMixin, ListView):
    model = MealPlan
    template_name = "foodplan/mealplan_list.html"
    paginate = 3

    def get_queryset(self):
        return MealPlan.objects.filter(user=self.request.user)

    def __str__(self):
        return str(self.name)


class MealplanDetailView(LoginRequiredMixin, DetailView):
    model = MealPlan
    template_name = "foodplan/detail.html"

    def get_queryset(self):
        return MealPlan.objects.filter(user=self.request.user)

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
    success_url = reverse_lazy("foodplan_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

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
        return MealPlan.objects.filter(user=self.request.user)

    def get_success_url(self) -> str:
        return reverse_lazy("foodplan_detail", args=[self.object.id])

    def __str__(self):
        return str(self.name)


class MealplanDeleteView(LoginRequiredMixin, DeleteView):
    model = MealPlan
    template_name = "foodplan/delete.html"
    success_url = reverse_lazy("foodplan_list")

    def get_queryset(self):
        return MealPlan.objects.filter(user=self.request.user)

    def __str__(self):
        return str(self.name)
