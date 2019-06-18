from django.http import Http404, request
from django.shortcuts import render
from vlance.models import  ThanhPho,Job
from django.views.generic import ListView , DetailView , CreateView ,UpdateView ,DeleteView



def index(request):
    return render(request, "index.html", {})

def dangviectuyendung(request):
    return render(request, "dang-viec-tuyen-dung.html", {})


def dangcuocthi(request):
    return render(request, "dang-cuoc-thi.html", {})

##### Viec lam .

def Viecfreelances(request, slug):
    try:
        VC = Job.objects.get(slug=slug)
    except Job.DoesNotExist:
        raise Http404("Loi bai viet roi !! Lien he DUC ngay !! ")
    return render(request, 'viec-freelance/index.html', {'VC': VC})
