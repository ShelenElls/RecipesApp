from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from recipes.models import Recipe
from tags.models import Tag


# Create your views here.
class TagListView(ListView):
    model = Tag
    template_name = "tags/list.html"
    paginate_by = 4

    def __str__(self):
        return str(self.name)


class TagDetailView(DetailView):
    model = Tag
    template_name = "tags/detail.html"

    def __str__(self):
        return str(self.name)


class TagCreateView(LoginRequiredMixin, CreateView):
    model = Tag
    template_name = "tags/new.html"
    fields = ["name", "recipes"]
    success_url = reverse_lazy("tags_list")

    def __str__(self):
        return str(self.name)


class TagUpdateView(UpdateView):
    model = Tag
    template_name = "tags/edit.html"
    fields = ["name", "recipes"]
    success_url = reverse_lazy("tags_list")

    def __str__(self):
        return str(self.name)


class TagDeleteView(DeleteView):
    model = Tag
    template_name = "tags/delete.html"
    success_url = reverse_lazy("tags_list")

    def __str__(self):
        return str(self.name)
