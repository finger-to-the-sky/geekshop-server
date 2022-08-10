from django.contrib import admin

from .models import ProductCategory, Product

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    search_fields = ('name',)
    ordering = ('name', 'price')