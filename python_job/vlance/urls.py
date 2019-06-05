from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path
from vlance import views
from vlance.views import ViecLamDetailView, Viecfreelances
from django.conf import settings


app_name = 'vlance'
urlpatterns = [
                  path('', views.index, name='index'),
                  path('dang-du-an', views.Postlist.as_view(), name='list'),
                  path('viec-lam-freelance', ViecLamDetailView.as_view(), name='lisst tesst'),
                  path('index.html', views.index, name='homepage'),
                  path('dang-du-an', views.dangduan, name='dang-du-an'),
                  path('dang-viec-tuyen-dung', views.dangviectuyendung, name='dang-viec-tuyen-dung'),
                  path('dang-cuoc-thi', views.dangcuocthi, name='dang-cuoc-thi'),
                  path('viec-lam-freelance', views.vieclamfreelance, name='viec-lam'),

                  path('viec-freelance/<str:slug>/', views.Viecfreelances, name='product'),

              ] + static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)

