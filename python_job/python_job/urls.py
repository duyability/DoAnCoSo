"""python_job URL Configuration

The `urlpatterns` list routes URLs to view. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function view
    1. Add an import:  from my_app import view
    2. Add a URL to urlpatterns:  path('', view.home, name='home')
Class-based view
    1. Add an import:  from other_app.view import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vlance.urls')),
    path('', include('accounts.urls')),
    path('', include('page.urls')),
    path('search/', include('search.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^admin/', include('dbbackup_ui.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_ALL, document_root=settings.MEDIA_ROOT)

#handler404 = 'perfect404.views.page_not_found'

