from django.urls import path

from page.views import PageList
from . import views

app_name = 'page'

urlpatterns = [
    path('blog/<str:slug>.html', views.PageDetail, name="page-detail"),
    path('blog/', PageList.as_view(), name="page-list-views"),
            ]
