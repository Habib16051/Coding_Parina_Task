from django.contrib import admin
from .models import SearchInput


@admin.register(SearchInput)
class SearchInputAdmin(admin.ModelAdmin):
    list_display = ('user', 'input_values', 'search_value', 'timestamp')
    list_filter = ('user', 'timestamp')
    search_fields = ('user__username', 'input_values', 'search_value')
