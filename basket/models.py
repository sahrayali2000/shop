from django.db import models
from products.models import Product
from members.models import Customer
from datetime import date, datetime
# Create your models here.

class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True, verbose_name='مشتری')
    title = models.CharField(max_length=500,verbose_name='عنوان آدرس', null=True)
    address_content = models.TextField(verbose_name='آدرس', null=True)
    class Meta:
        verbose_name = 'آدرس'
        verbose_name_plural = 'آدرس ها'
    def __str__(self):
        return self.title


class Basket(models.Model):
    product = models.ManyToManyField(Product, null=True, verbose_name='محصولات')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True, verbose_name='مشتری')
    total_amount = models.IntegerField(null=True, blank=True, verbose_name='مجموع قیمت')
    date = models.DateField(auto_now_add=True, verbose_name='تاریخ ثبت')
    final_amount = models.IntegerField(null=True, blank=True, verbose_name='قیمت نهایی')
    READY = 1
    SENT = 2
    DELIVERED = 3
    status_choices = (
        (READY, 'ready'),
        (SENT, 'sent'),
        (DELIVERED, 'delivered'),
    )
    status = models.IntegerField(choices=status_choices, default=1, verbose_name='وضعیت پردازش')
    address = models.ForeignKey(Address, on_delete=models.CASCADE, verbose_name='آدرس')

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبد های خرید'

    def __str__(self):
        return f'{self.customer.first_name} {self.customer.last_name} zip code : {self.customer.zip_code}'


class Coupon(models.Model):
    customers = models.ManyToManyField(Customer, null=True, verbose_name='مشتری ها')
    discount_percent = models.PositiveSmallIntegerField(verbose_name='درصد تخفیف')
    coupon_number = models.PositiveIntegerField( verbose_name='کد تخفیف')
    expire_date = models.DateField(null=True, blank=True, verbose_name='تاریخ انتقضا')
    is_active = models.BooleanField(default=True, verbose_name='وضعیت')
    class Meta:
        verbose_name = 'کد تخفیف'
        verbose_name_plural = 'کد های تخفیف '
    def __str__(self):
        return f'coupon number {self.coupon_number}'








