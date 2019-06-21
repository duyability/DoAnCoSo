from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView

from page.models import Page


def PageDetail(request, slug):
    try:
        p = Page.objects.get(slug=slug)
    except Page.DoesNotExist:
        raise Http404("Lỗi rồi !! Lien he DUC ngay !! ")
    return render(request, 'page.html', {'p': p})


class PageList(ListView):
    template_name = 'page-list.html'
    model = Page
    context_object_name = 'p'
    queryset = Page.objects.all()
    paginate_by = 4
