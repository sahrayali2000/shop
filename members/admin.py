from django.contrib import admin
from .models import Customer
# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'zip_code']
    search_fields = ['first_name', 'last_name']


