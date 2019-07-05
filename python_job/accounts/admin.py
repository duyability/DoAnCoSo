from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from accounts.models import User


################------USER------##############

class UserResource(resources.ModelResource):
    class Meta:
        model = User
        exclude = ('created_on','password','last_login','is_superuser','groups','user_permissions','is_staff','is_active','date_joined')

class UserAdmin(ImportExportModelAdmin):
    exclude = ['slug']
    list_display = ["first_name", "last_name","email","hotline", ]
    search_fields = ["first_name", "last_name","email","hotline","gender",]
    resource_class = UserResource


admin.site.register(User, UserAdmin)

##########################################################
