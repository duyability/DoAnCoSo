from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path
from vlance.view.NhaTuyenDung import JobCreateView, PartTimeCreateView
from vlance.view.freelance import ApplyJobView, ApplyCV
from vlance.views import index, dangcuocthi, DetaiOnsite, vieclamfreelance, Viecfreelances, vieclam, PartTime, \
    JobDetailsView, CVDetail
from django.conf import settings

app_name = 'vlance'
urlpatterns = [
                  path('', index, name='index'),
                  path('index.html', index, name='homepage'),
                  path('viec-lam-freelance', vieclam.as_view(), name='viec-lam-freelance'),
    # Part Time
                  path('viec-lam-onsite', PartTime.as_view(), name='Job-PartTime'),
                  path('viec-onsite/<str:slug>/', DetaiOnsite, name='viec-onsite'),


                  path('dang-viec-tuyen-dung', PartTimeCreateView.as_view(), name='dang-viec-tuyen-dung'),
                  path('dang-cuoc-thi', dangcuocthi, name='dang-cuoc-thi'),
                  path('viec-lam-freelance', vieclamfreelance, name='viec-lam'),

                  path('viec-freelance/<str:slug>/', Viecfreelances, name='product'),
                  path('dang-du-an/',JobCreateView.as_view(), name='dang-du-an'),
    # bao gia viec theo du an
                  path('bao-gia/<int:id>/', JobDetailsView.as_view(), name='jobs-detail'),
                  path('nop-cv-du-an/<int:job_id>/',ApplyJobView.as_view(), name='app-job'),
    # bao gia viec part time
                  path('nop-cv/<int:id>/', CVDetail.as_view(), name='cv-detail'),
                  path('nop-cv-pt/<int:jobpt_id>/', ApplyCV.as_view(), name='nop-cv-pt'),


              ] + static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)

