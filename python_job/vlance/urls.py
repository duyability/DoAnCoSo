from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path, include

from vlance.view.NhaTuyenDung import JobCreateView, PartTimeCreateView, DashboardView, ApplicantsListView, \
    ApplicantPerJobView, filled, DeleteJob, ChapnhanBaoGia, filleds, DeleteJobpt, ApplicantPerJPT, ChapnhanBaoGiaPT, \
    CuocThiCreateView, DeleteMess, CVonsiteListView, CuocThiList, filledss, ChapnhanCT, CuocThiListView
from vlance.view.freelance import ApplyJobView, ApplyCV, SuccessJob, SuccessJobpt, Successct, ApplyCT
from vlance.views import index, dangcuocthi, DetaiOnsite, vieclamfreelance, Viecfreelances, vieclam, PartTime, \
    JobDetailsView, CVDetail, detaiNN, detaiTP, detaiNNs, CuocThiView, CuocThiDetail, CTDetail
from django.conf import settings

app_name = 'vlance'
urlpatterns = [
                  path('', index, name='index'),
                  path('ckeditor/', include('ckeditor_uploader.urls')),
                  path('index.html', index, name='homepage'),
                  path('viec-lam-freelance', vieclam.as_view(), name='viec-lam-freelance'),
                  # Part Time
                  path('viec-lam-onsite', PartTime.as_view(), name='Job-PartTime'),
                  path('cuoc-thi-thiet-ke', CuocThiView.as_view(), name='Cuoc-Thi-Thiet-ke'),
                  path('cuoc-thi/<str:slug>', CuocThiDetail, name='Cuoc-Thi-Detail'),
                  path('viec-onsite/<str:slug>/', DetaiOnsite, name='viec-onsite'),

                  path('dang-viec-tuyen-dung', PartTimeCreateView.as_view(), name='dang-viec-tuyen-dung'),
                  path('dang-cuoc-thi', CuocThiCreateView.as_view(), name='dang-cuoc-thi'),
                  path('viec-lam-freelance', vieclamfreelance, name='viec-lam'),

                  path('viec-freelance/<str:slug>/', Viecfreelances, name='product'),

                  path('viec-lam-freelance/nn/<str:slug>', detaiNN, name='detail-nganh-nghe'),
                  path('viec-lam-onsite/nn/<str:slug>', detaiNN, name='detail-nganh-nghe-ons'),

                  path('viec-lam-freelance/tp/<str:slug>', detaiTP, name='detail-SS'),
                  path('viec-lam-onsite/tp/<str:slug>', detaiTP, name='detail-thanh-pho-s'),

                  path('dang-du-an/', JobCreateView.as_view(), name='dang-du-an'),
                  # bao gia viec theo du an
                  path('bao-gia/<int:id>/', JobDetailsView.as_view(), name='jobs-detail'),
                  path('nop-cv-du-an/<int:job_id>/', ApplyJobView.as_view(), name='app-job'),
                  # bao gia viec part time
                  path('nop-cv/<int:id>/', CVDetail.as_view(), name='cv-detail'),
                  path('nop-cv-pt/<int:jobpt_id>/', ApplyCV.as_view(), name='nop-cv-pt'),
                  #  nop bai thi
                  path('nop-bai-thi/<int:id>/', CTDetail, name='ct-detail'),
                  path('bai-du-thi/<int:ct_id>/', ApplyCT.as_view(), name='nop-bai-du-thi'),

                  # dashboard
                  path('nhatuyendung/dashboard/', include([
                      path('', DashboardView.as_view(), name='employer-dashboard'),
                      path('all-applicants', ApplicantsListView.as_view(), name='employer-all-applicants'),
                      path('all-cv', CVonsiteListView.as_view(), name='employer-all-cv'),
                      path('all-ct', CuocThiListView.as_view(), name='employer-all-ct'),


                      path('applicants/<int:job_id>', ApplicantPerJobView.as_view(),
                           name='employer-dashboard-applicants'),
                      path('applicant/<int:jobpt_id>', ApplicantPerJPT.as_view(),
                           name='employer-dashboard-applicants-pt'),
                      path('cuoc-thi/<int:ct_id>', CuocThiList.as_view(),
                           name='employser-dashboard-applicants-ct'),

                      path('cv-applicants/<int:applicant_id>', ChapnhanBaoGia.as_view(), name='chap-nhan-job'),
                      path('pt-applicants/<int:cvonsite_id>', ChapnhanBaoGiaPT.as_view(), name='chap-nhan-jobpt'),
                      path('ct-applicants/<int:bt_id>', ChapnhanCT.as_view(), name='chap-nhan-cuoc-thi'),  # ...........

                      path('mark-filled/<int:job_id>', filled, name='job-mark-filled'),
                      path('mark-filled-pt/<int:jobpt_id>', filleds, name='jobpt-mark-filled'),
                      path('mark-filled-ct/<int:ct_id>', filledss, name='cuoc-thi-mark-filled'),
                  ])),

                  # Success_BaoGia - Cuoc Thi
                  path('freelancer/job', SuccessJob.as_view(), name='Freelance-all-job'),
                  path('freelancer/jobpt', SuccessJobpt.as_view(), name='Freelance-all-job-part-time'),
                  path('freelancer/ct', Successct.as_view(), name='Freelance-all-cuoc-thi'),

                  # Delete
                  path('delete/<int:id>', DeleteJob.as_view(), name='job-delete'),
                  path('delete_jpt/<int:user_id>', DeleteJobpt.as_view(), name='jobpt-delete'),
                  path('delete_mess/<int:id>', DeleteMess.as_view(), name='mess-delete'),

              ] + static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)

