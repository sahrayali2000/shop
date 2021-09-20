from django.contrib import admin
from .models import Product, Category
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass
