from django.conf.urls import re_path
from .views import BackupView

urlpatterns = [
    re_path('^backup-database-and-media/$', BackupView.as_view(), name="backup_view"),
]