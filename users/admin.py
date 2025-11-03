from django.contrib import admin

from .models import CatalogUser


@admin.register(CatalogUser)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("email",)
    list_filter = ("email",)
    search_fields = ("email",)
