from django.contrib import admin
from .models import Customer, Staff
# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    pass