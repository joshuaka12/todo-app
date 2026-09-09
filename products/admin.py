from django.contrib import admin
from .models import products, Category
# Register your models here.

@admin.register(products)
# admin.site.register(Category)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id","user","price","stock","is_actvice", "in_sale", "created_at")
    list_filter = ("is_active", "in_sale", "created_at")
    search_field = ("name","description")
    ordering = "-created_at"
    #filter_horizontal + ("categories",)

def get_cate