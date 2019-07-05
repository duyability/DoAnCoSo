from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import redirect, get_object_or_404, render_to_response
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from vlance.decorators import user_is_employer, user_is_employee
from vlance.froms import CreateJobForm, PartTimeFrom, ChapnhanJob, ChapnhanJobpt, CuocThiFrom, Chapnhanbt
from vlance.models import Job, Applicant, GuiTBChapNhanJob, JobPartTime, CVonsite, GuiTBChapNhanJobpt, CuocThi, BaiThi, \
    GuiTBChapNhanct
from vlance.views import thanhpho


class DashboardView(ListView):
    model = Job
    template_name = 'tai-khoan/Nhatuyendung/dashboard.html'
    context_object_name = 'jobs'

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    @method_decorator(user_is_employer)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get_queryset(self):
        return self.model.objects.filter(user_id=self.request.user.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jpt'] = JobPartTime.objects.all()
        context['ct'] = CuocThi.objects.all()
        return context


class ApplicantPerJobView(ListView):
    model = Applicant
    template_name = 'tai-khoan/Nhatuyendung/appy_job.html'
    context_object_name = 'applicants'
    paginate_by = 1

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    @method_decorator(user_is_employer)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get_queryset(self):
        return Applicant.objects.filter(job_id=self.kwargs['job_id']).order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['job'] = Job.objects.get(id=self.kwargs['job_id'])
        return context


# ################################################################

class ApplicantPerJPT(ListView):
    model = CVonsite
    template_name = 'tai-khoan/Nhatuyendung/appy_jobpt.html'
    context_object_name = 'cvonsite'
    paginate_by = 5

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    @method_decorator(user_is_employer)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get_queryset(self):
        return CVonsite.objects.filter(jobpt_id=self.kwargs['jobpt_id']).order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jobpt'] = JobPartTime.objects.get(id=self.kwargs['jobpt_id'])
        return context


# ################################################################

class CuocThiList(ListView):
    model = BaiThi
    template_name = 'tai-khoan/Nhatuyendung/appy_ct.html'
    context_object_name = 'bt'
    paginate_by = 5

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    @method_decorator(user_is_employer)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get_queryset(self):
        return BaiThi.objects.filter(ct_id=self.kwargs['ct_id']).order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ct'] = CuocThi.objects.get(id=self.kwargs['ct_id'])
        return context


# #################################################################
# Viec theo du an by Đức
class JobCreateView(CreateView, thanhpho):
    template_name = 'dang-du-an.html'
    form_class = CreateJobForm
    extra_context = {
        'title': 'Post New Job'
    }
    success_url = reverse_lazy('vlance:viec-lam')

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return reverse_lazy('accounts:login')
        if self.request.user.is_authenticated and self.request.user.role != 'NhaTuyenDung':
            return reverse_lazy('accounts:login')
        return super().dispatch(self.request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(JobCreateView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


# Viec PartTime by Đức
class PartTimeCreateView(CreateView, thanhpho):
    template_name = 'dang-viec-tuyen-dung.html'
    form_class = PartTimeFrom
    extra_context = {
        'title': 'Post New Job'
    }
    success_url = reverse_lazy('vlance:Job-PartTime')

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return reverse_lazy('accounts:login')
        if self.request.user.is_authenticated and self.request.user.role != 'NhaTuyenDung':
            return reverse_lazy('accounts:login')
        return super().dispatch(self.request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PartTimeCreateView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


# ##############################################
# Viec PartTime by Đức

class CuocThiCreateView(CreateView):
    template_name = 'dang-cuoc-thi.html'
    form_class = CuocThiFrom
    extra_context = {
        'title': 'Post New Cuoc Thi'
    }
    success_url = reverse_lazy('vlance:Cuoc-Thi-Thiet-ke')

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated and self.request.user.role != 'NhaTuyenDung':
            return reverse_lazy('vlance:Cuoc-Thi-Thiet-ke')
        if not self.request.user.is_authenticated:
            return reverse_lazy('accounts:login')
        return super().dispatch(self.request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CuocThiCreateView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


############################
# ALL tin đăng dự án
############################

class ApplicantsListView(ListView):
    model = Applicant
    template_name = 'tai-khoan/Nhatuyendung/all_appy_job.html'
    context_object_name = 'applicants'
    paginate_by = 5

    def get_queryset(self):
        return self.model.objects.filter(job__user_id=self.request.user.id)


################################
# ALL tin đăng việc part time
###############################

class CVonsiteListView(ListView):
    model = CVonsite
    template_name = 'tai-khoan/Nhatuyendung/all_job_part_time.html'
    context_object_name = 'cvonsite'
    paginate_by = 5

    def get_queryset(self):
        return self.model.objects.filter(jobpt__user_id=self.request.user.id)


################################
# ALL cuoc thi
###############################

class CuocThiListView(ListView):
    model = BaiThi
    template_name = 'tai-khoan/Nhatuyendung/all_job_cuoc-thi.html'
    context_object_name = 'baithi'
    paginate_by = 5

    def get_queryset(self):
        return self.model.objects.filter(ct__user_id=self.request.user.id)


@login_required(login_url=reverse_lazy('accounts:login'))
def filled(request, job_id=None):
    job = Job.objects.get(user_id=request.user.id, id=job_id)
    job.filled = True
    job.save()
    return HttpResponseRedirect(reverse_lazy('vlance:employer-dashboard'))


@login_required(login_url=reverse_lazy('accounts:login'))
def filleds(request, jobpt_id=None):
    jobpt = JobPartTime.objects.get(user_id=request.user.id, id=jobpt_id)
    jobpt.filled = True
    jobpt.save()
    return HttpResponseRedirect(reverse_lazy('vlance:employer-dashboard'))


@login_required(login_url=reverse_lazy('accounts:login'))
def filledss(request, ct_id=None):
    ct = CuocThi.objects.get(user_id=request.user.id, id=ct_id)
    ct.filled = True
    ct.save()
    return HttpResponseRedirect(reverse_lazy('vlance:employer-dashboard'))


# ################# Delete ##############################
class DeleteJob(DeleteView):
    template_name = 'tags/delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Job, id=id_)

    def get_success_url(self):
        return reverse('vlance:employer-dashboard')


class DeleteJobpt(DeleteView):
    template_name = 'tags/delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(JobPartTime, id=id_)

    def get_success_url(self):
        return reverse('vlance:employer-dashboard')


class DeleteMess(DeleteView):
    template_name = 'tags/delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(GuiTBChapNhanJob, id=id_)

    def get_success_url(self):
        return reverse('vlance:Freelance-all-job')


# ##########################################

class ChapnhanBaoGia(CreateView):
    model = GuiTBChapNhanJob
    template_name = 'tai-khoan/Nhatuyendung/appy_job.html'
    form_class = ChapnhanJob
    extra_context = {
        'title': 'Post New Job'
    }
    slug_field = 'applicant_id'
    slug_url_kwarg = 'applicant_id'
    success_url = reverse_lazy('vlance:homepage')

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return reverse_lazy('accounts:login')
        return super().dispatch(self.request, *args, **kwargs)

    def form_valid(self, form):
        # check if user already applied
        c = GuiTBChapNhanJob.objects.filter(user_id=self.request.user.id, applicant_id=self.kwargs['applicant_id'])
        if c:
            messages.info(self.request, 'Bạn đã gửi báo giá cho công việc này')
            return HttpResponseRedirect(self.get_success_url())
        # save applicant
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


# #############################################################

class ChapnhanBaoGiaPT(CreateView):
    model = GuiTBChapNhanJobpt
    template_name = 'tai-khoan/Nhatuyendung/appy_jobpt.html'
    form_class = ChapnhanJobpt
    extra_context = {
        'title': 'Post New Job'
    }
    slug_field = 'cvonsite_id'
    slug_url_kwarg = 'cvonsite_id'
    success_url = reverse_lazy('vlance:homepage')

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return reverse_lazy('accounts:login')
        return super().dispatch(self.request, *args, **kwargs)

    def form_valid(self, form):
        # check if user already applied
        c = GuiTBChapNhanJobpt.objects.filter(user_id=self.request.user.id, cvonsite_id=self.kwargs['cvonsite_id'])
        if c:
            messages.info(self.request, 'Bạn đã gửi báo giá cho công việc này')
            return HttpResponseRedirect(self.get_success_url())
        # save applicant
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


# #############################################################

class ChapnhanCT(CreateView):
    model = GuiTBChapNhanct
    template_name = 'tai-khoan/Nhatuyendung/appy_ct.html'
    form_class = Chapnhanbt
    extra_context = {
        'title': 'Post New Job'
    }
    slug_field = 'bt_id'
    slug_url_kwarg = 'bt_id'
    success_url = reverse_lazy('vlance:homepage')

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return reverse_lazy('accounts:login')
        return super().dispatch(self.request, *args, **kwargs)

    def form_valid(self, form):
        # check if user already applied
        c = GuiTBChapNhanct.objects.filter(user_id=self.request.user.id, bt_id=self.kwargs['bt_id'])
        if c:
            messages.info(self.request, 'Bạn đã gửi báo giá cho công việc này')
            return HttpResponseRedirect(self.get_success_url())
        # save applicant
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
