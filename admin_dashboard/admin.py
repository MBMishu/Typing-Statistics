from django.contrib import admin

# Register your models here.
from .models import *


class AdminUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'role')
    list_filter = ('role',)
    search_fields = ('name', 'email', 'user', )


class GuestUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'role')
    list_filter = ('role',)
    search_fields = ('name', 'email', 'user', )


class PDFFileAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(PDFFile, PDFFileAdmin)
admin.site.register(AdminUser, AdminUserAdmin)
admin.site.register(GuestUser, GuestUserAdmin)
admin.site.register(UserData)
admin.site.register(FormData)
