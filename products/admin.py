from django.contrib import admin
from .models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "user",
        "price",
        "is_active",
        "in_sale",
        "created_at",
    )

    list_filter = (
        "is_active",
        "in_sale",
        "created_at",
    )

    search_fields = (
        "name",
        "description",
    )

    ordering = ("-created_at",)


admin.site.register(Category)