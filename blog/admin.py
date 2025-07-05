from django.contrib import admin
from .models import Post


@admin.register(Post)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("header", "content", "preview", "created_at", "publication_attribute", "views_counter")
    list_filter = ("header",)
    search_fields = ("header", "content")