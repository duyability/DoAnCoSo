from django.contrib import admin
from .models import Job, ThanhPho, NganhNghe, Applicant, JobPartTime, CVonsite, KyNang, GuiTBChapNhanJob, \
    GuiTBChapNhanJobpt


class exc(admin.ModelAdmin):
    exclude = ['slug', ]


class j(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ["title", "slug",'filled','id']
    exclude = ['slug']


admin.site.register(Job, j)

admin.site.register(ThanhPho, exc)
admin.site.register(NganhNghe, exc)
admin.site.register(Applicant)
admin.site.register(JobPartTime, j)
admin.site.register(CVonsite)
admin.site.register(KyNang)
admin.site.register(GuiTBChapNhanJob)
admin.site.register(GuiTBChapNhanJobpt)
