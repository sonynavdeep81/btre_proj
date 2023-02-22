from django.contrib import admin
from .models import Realtor


class RealtorAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_mvp']
    list_filter = ['name']
    list_editable = ['is_mvp']
    list_per_page = 3
    search_fields = ['name',]


admin.site.register(Realtor, RealtorAdmin)
