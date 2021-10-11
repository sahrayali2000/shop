from django.db import models
from products.models import Product
from members.models import Customer
from datetime import date, datetime
# Create your models here.

class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=500,verbose_name='عنوان آدرس', null=True)
    address_content = models.TextField(verbose_name='آدرس', null=True)

    def __str__(self):
        return self.title


class Basket(models.Model):
    product = models.ManyToManyField(Product, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    total_amount = models.IntegerField(null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    final_amount = models.IntegerField(null=True, blank=True)
    READY = 1
    SENT = 2
    DELIVERED = 3
    status_choices = (
        (READY, 'ready'),
        (SENT, 'sent'),
        (DELIVERED, 'delivered'),
    )
    status = models.IntegerField(choices=status_choices, default=1)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, verbose_name='آدرس')

    def __str__(self):
        return f'{self.customer.first_name} {self.customer.last_name} zip code : {self.customer.zip_code}'


class Coupon(models.Model):
    customers = models.ManyToManyField(Customer, null=True)
    discount_percent = models.PositiveSmallIntegerField()
    coupon_number = models.PositiveIntegerField()
    expire_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'coupon number {self.coupon_number}'






