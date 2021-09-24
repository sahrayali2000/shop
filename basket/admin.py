from django.contrib import admin
from .models import Basket, Coupon


# Register your models here.
@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    pass

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    pass