from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path
from vlance.view.NhaTuyenDung import JobCreateView, PartTimeCreateView
from vlance.view.freelance import ApplyJobView
from vlance.views import index, dangcuocthi, DetaiOnsite, vieclamfreelance, Viecfreelances, vieclam, PartTime, \
    JobDetailsView
from django.conf import settings

app_name = 'vlance'
urlpatterns = [
                  path('', index, name='index'),
                  path('viec-lam-freelance', vieclam.as_view(), name='viec-lam-freelance'),
                  path('viec-lam-onsite', PartTime.as_view(), name='Job-PartTime'),
                  path('index.html', index, name='homepage'),
                  path('dang-viec-tuyen-dung', PartTimeCreateView.as_view(), name='dang-viec-tuyen-dung'),
                  path('dang-cuoc-thi', dangcuocthi, name='dang-cuoc-thi'),
                  path('viec-lam-freelance', vieclamfreelance, name='viec-lam'),
                  path('viec-onsite/<str:slug>/', DetaiOnsite, name='viec-onsite'),
                  path('viec-freelance/<str:slug>/', Viecfreelances, name='product'),
                  path('dang-du-an/',JobCreateView.as_view(), name='dang-du-an'),
    # bao gia viec theo du an
                  path('bao-gia/<int:id>/', JobDetailsView.as_view(), name='jobs-detail'),
                  path('nop-cv-du-an/<int:job_id>/',ApplyJobView.as_view(), name='app-job'),
    # bao gia viec part time


              ] + static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)

