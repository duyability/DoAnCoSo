from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from vlance.view.freelance import EditProfileView
from .views import *

app_name = "accounts"

urlpatterns = [
    path('tai-khoan/freelance', RegisterEmployeeView.as_view(), name='employee-register'),
    path('tai-khoan/nhatuyendung', RegisterEmployerView.as_view(), name='employer-register'),
    path('employee/profile/update', EditProfileView.as_view(), name='employer-profile-update'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('login', LoginView.as_view(), name='login'),
]+ static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)
