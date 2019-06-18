from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from vlance.view.freelance import EditProfileView , EditProfileCVView
from .views import *

app_name = "accounts"


urlpatterns = [
    path('tai-khoan/freelance', RegisterEmployeeView.as_view(), name='employee-register'),
    path('tai-khoan/nhatuyendung', RegisterEmployerView.as_view(), name='employer-register'),

    #update-edit
    path('tai-khoan/freelance/update-basic', EditProfileView.as_view(), name='employer-profile-update'),
    path('tai-khoan/freelance/update-cv', EditProfileCVView.as_view(), name='employer-profile-cv'),

    #login
    path('logout', LogoutView.as_view(), name='logout'),
    path('login', LoginView.as_view(), name='login'),

    #detail
    path('freelancers', DsFreelance.as_view(), name='freelance'),
    path('freelancer/<int:id>', DetaiFreelance, name='info-freelance'),
]+ static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)
