from django.http import Http404
from django.shortcuts import render
from .models import DichVu, LinhVuc, ThanhPho, ViecTheoDuAn, KyNang
from django.views.generic import ListView , DetailView , CreateView ,UpdateView ,DeleteView
from django.utils import timezone
from django.views.generic.detail import DetailView


# Create your views here.

def index(request):
    return render(request, "index.html", {})


def dangduan(request):
    return render(request, "dang-du-an.html", {})


def dangviectuyendung(request):
    return render(request, "dang-viec-tuyen-dung.html", {})


def dangcuocthi(request):
    return render(request, "dang-cuoc-thi.html", {})

##### Viec lam .

def vieclamfreelance(request):
    return render(request, "viec-lam-freelance.html", {})


# Danh sach List
class Postlist(ListView):
    template_name = 'dang-du-an.html'
    model = DichVu
    context_object_name = 'post'
    queryset = DichVu.objects.all()

    def get_context_data(self, **kwargs):
        context = super(Postlist,self).get_context_data(**kwargs)
        context['thanhphos'] = ThanhPho.objects.all()
        context['post1'] = LinhVuc.objects.all()
        return context

#Lisst viec lam freelance

class ViecLamDetailView(ListView):
    template_name = 'viec-lam-freelance.html'
    model = ViecTheoDuAn
    context_object_name = 'VL'
    queryset = ViecTheoDuAn.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ViecLamDetailView,self).get_context_data(**kwargs)
        context['tp'] = ThanhPho.objects.all()
        context['lv'] = LinhVuc.objects.all()
        context['kn'] = KyNang.objects.all()

        return context


class ViecLamDetailView(ListView):
    template_name = 'viec-lam-freelance.html'
    model = ViecTheoDuAn
    context_object_name = 'VL'
    queryset = ViecTheoDuAn.objects.all()


def Viecfreelances(request, slug):
    try:
        VC = ViecTheoDuAn.objects.get(slug=slug)
    except ViecTheoDuAn.DoesNotExist:
        raise Http404("Loi bai viet roi !! Lien he DUC ngay !! ")
    return render(request, 'viec-freelance/index.html', {'VC': VC})
