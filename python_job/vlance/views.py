
from django.http import Http404, request
from django.shortcuts import render, get_object_or_404

from django.views.generic import CreateView, ListView
from vlance.models import Job, ThanhPho, NganhNghe, JobPartTime


# Create your view here.

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
#Lisst viec lam freelance

class thanhpho(ListView):
    model = ThanhPho
    context_object_name = 'tp'
    queryset = ThanhPho.objects.all()

    def get_context_data(self, **kwargs):
        context = super(thanhpho,self).get_context_data(**kwargs)
        context['nghe'] = NganhNghe.objects.all()
        return context

# Việc Làm Dự án
class vieclam(ListView):
    template_name = 'viec-lam-freelance.html'
    paginate_by = 1
    model = Job
    context_object_name = 'vl'
    queryset = Job.objects.all()

    def get_context_data(self, **kwargs):
        context = super(vieclam,self).get_context_data(**kwargs)
        context['tp'] = ThanhPho.objects.all()
        context['NN'] = NganhNghe.objects.all()
        return context



def Viecfreelances(request, slug):
    try:
        VC = Job.objects.get(slug=slug)
    except Job.DoesNotExist:
        raise Http404("Loi bai viet roi !! Lien he DUC ngay !! ")
    return render(request, 'viec-freelance/index.html', {'VC': VC})


# Việc làm Part Time
class PartTime(ListView):
    template_name = 'viec-lam-onsite.html'
    paginate_by = 5
    model = JobPartTime
    context_object_name = 'JPT'
    queryset = JobPartTime.objects.all()

    def get_context_data(self, **kwargs):
        context = super(PartTime,self).get_context_data(**kwargs)
        context['tp'] = ThanhPho.objects.all()
        context['NN'] = NganhNghe.objects.all()
        return context



def DetaiOnsite(request, slug):
    try:
        jp = JobPartTime.objects.get(slug=slug)
    except JobPartTime.DoesNotExist:
        raise Http404("Lỗi rồi !! Lien he DUC ngay !! ")
    return render(request, 'viec-freelance/viec-onsite.html', {'jp': jp})
