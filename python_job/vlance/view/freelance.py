from django.contrib.auth.decorators import login_required
from django.contrib.messages.context_processors import messages
from django.core.checks import messages
from django.http import Http404, HttpResponseRedirect, request
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView, CreateView, ListView
from accounts.forms import ProfileUpdateBasic, ProfileUpdateCV
from accounts.models import User
from vlance.decorators import user_is_employee, user_is_employer
from vlance.froms import ApplyJobForm, ApplyCVForm, BaiThiFrom
from vlance.models import Applicant, Job, CVonsite, NganhNghe, ThanhPho, KyNang, GuiTBChapNhanJob, BaiThi, \
    GuiTBChapNhanJobpt, GuiTBChapNhanct, CuocThi
from vlance.views import thanhpho


class EditProfileView(UpdateView):
    model = User
    form_class = ProfileUpdateBasic
    context_object_name = 'f'
    template_name = 'tai-khoan/Freelance/edituser.html'
    success_url = reverse_lazy('accounts:employer-profile-update')

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    # @method_decorator(user_is_employer)
    # @method_decorator(user_is_employee)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            raise Http404("User doesn't exists")
        # context = self.get_context_data(object=self.object)
        return self.render_to_response(self.get_context_data())

    def get_object(self, queryset=None):
        obj = self.request.user
        print(obj)
        if obj is None:
            raise Http404("Job doesn't exists")
        return obj

    # def post(self, request, *args, **kwargs):
    #     form = self.get_form()
    #     if form.is_valid():
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)


# update cv

class EditProfileCVView(UpdateView):
    model = User
    form_class = ProfileUpdateCV
    context_object_name = 'f'
    template_name = 'tai-khoan/Freelance/editdetail.html'
    success_url = reverse_lazy('accounts:employer-profile-cv')

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    # @method_decorator(user_is_employer)
    # @method_decorator(user_is_employee)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            raise Http404("User doesn't exists")
        # context = self.get_context_data(object=self.object)
        return self.render_to_response(self.get_context_data())

    def get_object(self, queryset=None):
        obj = self.request.user
        print(obj)
        if obj is None:
            raise Http404("Job doesn't exists")
        return obj


# Gui bao gia
class ApplyJobView(CreateView):
    model = Applicant
    template_name = 'from/cv-jop.html'
    form_class = ApplyJobForm
    slug_field = 'job_id'
    slug_url_kwarg = 'job_id'
    extra_context = {
        'title': 'Post New Job'
    }
    success_url = reverse_lazy('vlance:homepage')

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return reverse_lazy('accounts:login')
        return super().dispatch(self.request, *args, **kwargs)

    def form_valid(self, form):
        # check if user already applied
        applicant = Applicant.objects.filter(user_id=self.request.user.id, job_id=self.kwargs['job_id'])
        if applicant:
            messages.INFO(self.request, 'Bạn đã gửi báo giá cho công việc này')
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


# Gui CV cng viec PartTime

class ApplyCV(CreateView):
    model = CVonsite
    template_name = 'from/cv-onsite.html'
    form_class = ApplyCVForm
    slug_field = 'jobpt_id'
    slug_url_kwarg = 'jobpt_id'
    extra_context = {
        'title': 'Post New Job'
    }
    success_url = reverse_lazy('vlance:homepage')

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return reverse_lazy('accounts:login')
        return super().dispatch(self.request, *args, **kwargs)

    def form_valid(self, form):
        # check if user already applied
        applicant = CVonsite.objects.filter(user_id=self.request.user.id, jobpt_id=self.kwargs['jobpt_id'])
        if applicant:
            messages.Info(self.request, 'Bạn đã gửi báo giá cho công việc này')
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


# Gui CV cng viec PartTime

class ApplyCT(CreateView):
    model = BaiThi
    template_name = 'from/bai-du-thi.html'
    form_class = BaiThiFrom
    slug_field = 'ct_id'
    slug_url_kwarg = 'ct_id'
    extra_context = {
        'title': 'Post New Job'
    }
    success_url = reverse_lazy('vlance:homepage')

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return reverse_lazy('accounts:login')
        return super().dispatch(self.request, *args, **kwargs)

    def form_valid(self, form):
        # check if user already applied
        cts = BaiThi.objects.filter(user_id=self.request.user.id, ct_id=self.kwargs['ct_id'])
        if cts:
            messages.Info(self.request, 'Bạn đã bai thi này')
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
# Gui bai thi

class BaiThiCre(CreateView):
    model = BaiThi
    template_name = 'from/cv-onsite.html'
    form_class = BaiThiFrom
    slug_field = 'ct_id'
    slug_url_kwarg = 'ct_id'
    extra_context = {
        'title': 'Gửi Bài Thi'
    }
    success_url = reverse_lazy('vlance:homepage')

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return reverse_lazy('accounts:login')
        return super().dispatch(self.request, *args, **kwargs)

    def form_valid(self, form):
        # check if user already applied
        applicant = CVonsite.objects.filter(user_id=self.request.user.id, jobpt_id=self.kwargs['ct_id'])
        if applicant:
            messages.Info(self.request, 'Bạn đã gửi báo giá cho công việc này')
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


# ######## THONG BAO NHAN JOB THANH CONG #############################
class SuccessJob(ListView):
    model = GuiTBChapNhanJob
    template_name = 'tai-khoan/Freelance/success_job.html'
    context_object_name = 'success'
    paginate_by = 5

    def get_queryset(self):
        return self.model.objects.filter(applicant__user_id=self.request.user.id)


####### Job PartTime########

class SuccessJobpt(ListView):
    model = GuiTBChapNhanJobpt
    template_name = 'tai-khoan/Freelance/success_jobpt.html'
    context_object_name = 'pt'
    paginate_by = 5

    def get_queryset(self):
        return self.model.objects.filter(cvonsite__user_id=self.request.user.id)


####### Cuộc Thi########

class Successct(ListView):
    model = GuiTBChapNhanct
    template_name = 'tai-khoan/Freelance/success_ct.html'
    context_object_name = 'success'
    paginate_by = 5

    def get_queryset(self):
        return self.model.objects.filter(bt__user_id=self.request.user.id)
