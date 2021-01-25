from django.contrib import admin
from django.urls import path
from .models import *
from SMP.views import new_smp


@admin.register(SMP)
class SMPAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def get_urls(self):
        urls = super().get_urls()
        urls = [
                   path('add_smp/', self.admin_site.admin_view(new_smp))
               ] + urls
        return urls


@admin.register(SMP_des)
class SMP_desAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False
