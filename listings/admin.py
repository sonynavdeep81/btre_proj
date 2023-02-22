from django.contrib import admin
from .models import Listing


class ListingsAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'city',
                    'state', 'zipcode', 'is_published']
    list_display_links = ['title', 'city']
    list_filter = ['price', 'state']
    search_fields = ['zipcode']


admin.site.register(Listing, ListingsAdmin)
