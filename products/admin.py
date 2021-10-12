from django.contrib import admin
from .models import Product, Category
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'inventory']
    list_filter = ['category']
