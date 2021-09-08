from django.db import models
from product.models import Product
from members.models import Customer
# Create your models here.
class Basket(models.Model):
    product = models.ManyToManyField(Product, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    total_amount = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    have_discount = models.BooleanField(default=False)
    final_amount = models.IntegerField(null=True, blank=True)
    READY = 1
    SENT = 2
    DELIVERED = 3
    status_choices = (
        (READY, 'ready'),
        (SENT, 'sent'),
        (DELIVERED, 'delivered'),
    )
    status = models.IntegerField(choices=status_choices)

    def __str__(self):
        return f'{self.customer.first_name} {self.customer.last_name} {self.total_amount}'

class OrderHistory(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)


