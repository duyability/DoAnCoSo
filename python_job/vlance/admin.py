from django.contrib import admin
from .models import Job, ThanhPho, NganhNghe, Applicant, JobPartTime, CVonsite, KyNang, GuiTBChapNhanJob, \
    GuiTBChapNhanJobpt


class exc(admin.ModelAdmin):
    exclude = ['slug',]


admin.site.register(Job)
admin.site.register(ThanhPho,exc)
admin.site.register(NganhNghe,exc)
admin.site.register(Applicant)
admin.site.register(JobPartTime)
admin.site.register(CVonsite)
admin.site.register(KyNang)
admin.site.register(GuiTBChapNhanJob)
admin.site.register(GuiTBChapNhanJobpt)