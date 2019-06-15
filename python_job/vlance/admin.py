from django.contrib import admin
from .models import Job, ThanhPho, NganhNghe, Applicant, JobPartTime

admin.site.register(Job)
admin.site.register(ThanhPho)
admin.site.register(NganhNghe)
admin.site.register(Applicant)
admin.site.register(JobPartTime)

