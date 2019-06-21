from django.contrib import admin
# Register your models here.
from page.models import Page


class exc(admin.ModelAdmin):
    exclude = ['slug',]


admin.site.register(Page,exc)