from django.contrib import admin
from .models import Basket, Coupon, Address
from django.utils.html import format_html
from django.urls import reverse

# Register your models here.
def linkify(field_name):
    """
    Converts a foreign key value into clickable links.

    If field_name is 'parent', link text will be str(obj.parent)
    Link will be admin url for the admin url for obj.parent.id:change
    """

    def _linkify(obj):
        linked_obj = getattr(obj, field_name)
        if linked_obj is None:
            return '-'
        app_label = linked_obj._meta.app_label
        model_name = linked_obj._meta.model_name
        view_name = f'admin:{app_label}_{model_name}_change'
        link_url = reverse(view_name, args=[linked_obj.pk])
        return format_html('<a href="{}">{}</a>', link_url, linked_obj)

    _linkify.short_description = field_name  # Sets column name
    return _linkify


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ['customer', 'status',linkify('address')]
    list_filter = ['date']
    search_fields = ['date']


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ['coupon_number','is_active']
    filter_horizontal = ['customers']
    search_fields = ['coupon_number']


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['customer', 'title']
    search_fields = ['title']
