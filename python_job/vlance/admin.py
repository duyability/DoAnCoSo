from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Job, ThanhPho, NganhNghe, Applicant, JobPartTime, CVonsite, KyNang, GuiTBChapNhanJob, \
    GuiTBChapNhanJobpt, BaiThi, CuocThi


class exc(admin.ModelAdmin):
    exclude = ['slug', ]


class j(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ["title", "slug", 'filled', 'id']
    exclude = ['slug']


# ##################
#
# Xuat Nhap Khau
#
######################

###################------JOB PART TIME------###################

class PTResource(resources.ModelResource):
    class Meta:
        model = JobPartTime
        #fields = ('') #tuy chon data de xuat ra
        #export_order = ('') # sap xep lai thu tu
        #exclude = ('created_on') # loai bo                                                                                            #
class JPTAdmin(ImportExportModelAdmin):
    exclude = ['slug']
    list_display = ["title", "slug", 'filled',]
    resource_class = PTResource
admin.site.register(JobPartTime, JPTAdmin)

###############################################################

###################------JOB PART TIME------###################

class JobResource(resources.ModelResource):
    class Meta:
        model = Job                                                                                                                             #
class JAdmin(ImportExportModelAdmin):
    exclude = ['slug']
    list_display = ["title", "slug", 'filled',]
    resource_class = JobResource
admin.site.register(Job, JAdmin)

###############################################################

################------CUOC THI THIET KE------##############

class CTResource(resources.ModelResource):
    class Meta:
        model = CuocThi                                                                                                                             #
class CAdmin(ImportExportModelAdmin):
    exclude = ['slug']
    list_display = ["title", "slug", 'filled',]
    resource_class = CTResource
admin.site.register(CuocThi, CAdmin)

##########################################################

################------THANH PHO------##############

class TPResource(resources.ModelResource):
    class Meta:
        model = ThanhPho

        exclude = ('created_on','slug',)
class TPAdmin(ImportExportModelAdmin):
    exclude = ['slug']
    list_display = ["title", "slug",]
    resource_class = TPResource
admin.site.register(ThanhPho, TPAdmin)

##########################################################

################------Nganh Nghe------##############

class NNResource(resources.ModelResource):
    class Meta:
        model = NganhNghe
        exclude = ('created_on', 'slug',)

class NNAdmin(ImportExportModelAdmin):
    exclude = ['slug']
    list_display = ["title", "slug", ]
    resource_class = NNResource

admin.site.register(NganhNghe, NNAdmin)

##########################################################

################------Ky Nang------##############

class SkillResource(resources.ModelResource):
    class Meta:
        model = KyNang
        exclude = ('created_on', 'slug',)

class KyNangAdmin(ImportExportModelAdmin):
    exclude = ['slug']
    list_display = ["title", "slug", ]
    resource_class = SkillResource

admin.site.register(KyNang, KyNangAdmin)

##########################################################

admin.site.register(Applicant)
admin.site.register(CVonsite)
admin.site.register(GuiTBChapNhanJob)
admin.site.register(GuiTBChapNhanJobpt)
admin.site.register(BaiThi)

