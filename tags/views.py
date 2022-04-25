from django.shortcuts import render

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
