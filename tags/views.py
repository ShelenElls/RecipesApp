from django.shortcuts import render
from django.views.generic.base import TemplateView

try:
    from tags.models import Tag
except Exception:
    Tag = None


# Create your views here.
def show_tags(request):
    context = {
        "tags": Tag.objects.all() if Tag else None,
    }
    return render(request, "tags/list.html", context)


class MarkDown(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        markdowntext = open(
            os.path.join(os.path.dirname(__file__), "templates/test.md")
        ).read()

        context = super().get_context_data(**kwargs)
        context["markdowntext"] = markdowntext

        return context
