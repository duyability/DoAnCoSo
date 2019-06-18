from django.contrib import admin
from accounts.models import User,UpUser


class D(admin.ModelAdmin):
    search_fields = ['email']

admin.site.register(User,D)
admin.site.register(UpUser)
