from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path
from vlance.view.NhaTuyenDung import JobCreateView
from vlance.views import index, dangcuocthi, dangviectuyendung, vieclamfreelance, Viecfreelances, vieclam
from django.conf import settings

app_name = 'vlance'
urlpatterns = [
                  path('', index, name='index'),
                  path('viec-lam-freelance', vieclam.as_view(), name='lisst tesst'),
                  path('index.html', index, name='homepage'),
                  path('dang-viec-tuyen-dung', dangviectuyendung, name='dang-viec-tuyen-dung'),
                  path('dang-cuoc-thi', dangcuocthi, name='dang-cuoc-thi'),
                  path('viec-lam-freelance', vieclamfreelance, name='viec-lam'),
                  path('viec-freelance/<str:slug>/', Viecfreelances, name='product'),
                  path('dang-du-an/',JobCreateView.as_view(), name='dang-du-an'),
             ] + static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)

