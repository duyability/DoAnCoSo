from django.contrib.auth.decorators import login_required
from django.http import Http404, request, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from django.views.generic import CreateView, ListView, DetailView, UpdateView
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
        context['jobs'] = Job.objects.all()
        return context


# Việc Làm Dự án
class vieclam(ListView):
    template_name = 'viec-lam-freelance.html'
    paginate_by = 5
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

class JobDetailsView(DetailView):
    model = Job
    template_name = 'from/cv-jop.html'
    context_object_name = 'job'
    pk_url_kwarg = 'id'

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get_object(self, queryset=None):
        obj = super(JobDetailsView, self).get_object(queryset=queryset)
        if obj is None:
            raise Http404("Job doesn't exists")
        return obj

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            # redirect here
            raise Http404("Job doesn't exists")
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


# ### Detail CV Job PartTime ########

class CVDetail(DetailView):
    model = JobPartTime
    template_name = 'from/cv-onsite.html'
    context_object_name = 'jobpt'
    pk_url_kwarg = 'id'

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get_object(self, queryset=None):
        obj = super(CVDetail, self).get_object(queryset=queryset)
        if obj is None:
            raise Http404("Job doesn't exists")
        return obj

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            # redirect here
            raise Http404("Job doesn't exists")
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

def DetaiOnsite(request, slug):
    try:
        jp = JobPartTime.objects.get(slug=slug)
    except JobPartTime.DoesNotExist:
        raise Http404("Lỗi rồi !! Lien he DUC ngay !! ")
    return render(request, 'viec-freelance/viec-onsite.html', {'jp': jp})



# class detaiNN(ListView):
#     model = Job
#     template_name = 'viec-freelance/nganhnghe.html'
#     context_object_name = 'vl'
#
#     def get_queryset(self):
#         jobs = Job.objects.filter(Nganh_Nghe_slug=self.request.Nganh_Nghe_slug)
#         return jobs




