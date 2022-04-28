from ast import Delete
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from foodplan.models import Mealplan


class MealplanListView(LoginRequiredMixin, ListView):
    model = Mealplan
    template_name = "mealplan/list.html"

    def get_queryset(self):
        return Mealplan.objects.filter(owner=self.request.user)


class MealplanDetailView(LoginRequiredMixin, DetailView):
    model = DetailView
    template_name = "mealplan/detail.html"

    def get_queryset(self):
        return Mealplan.objects.filter(owner=self.request.user)


class MealplanCreateView(LoginRequiredMixin, CreateView):
    model = CreateView
    template_name = "mealplan/new.html"
    fields = [list of fields for user to create]

    def form_valid(self, form):
        plan = form.save(commit=False)
        plan.owner = self.request.user
        plan.save()
        form.save_m2m()
        return redirect("mealplan_detail", pk=plan.id)


class MealplanUpdateView(LoginRequiredMixin, UpdateView):
    model = UpdateView
    template_name = "mealplan/edit.html"
    fields = [list of fields for user to create]

    def get_queryset(self):
        return Mealplan.objects.filter(owner=self.request.user)

    def get_success_url(self) -> str:
        return reverse_lazy("mealplan_detail", args=[self.object.id])


class MealplanDeleteView(LoginRequiredMixin, DeleteView):
    model = Delete
    template_name = "mealplan/delete.html"
    success_url = reverse_lazy("mealplan_list")

    def get_queryset(self):
        return Mealplan.objects.filter(owner=self.request.user)