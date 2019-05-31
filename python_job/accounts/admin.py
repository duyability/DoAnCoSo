from django.contrib import admin
from accounts.models import User


class D(admin.ModelAdmin):
    search_fields = ['email']

admin.site.register(User,D)
