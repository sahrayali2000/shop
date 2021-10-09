from django.contrib.auth import get_user_model
from django.db import models


gotten_user = get_user_model()
# Create your models here.

class Staff(models.Model):
    user = models.OneToOneField(gotten_user, on_delete=models.CASCADE, related_name='StaffUser')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    emp_code = models.IntegerField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Customer(models.Model):
    user = models.OneToOneField(gotten_user, on_delete=models.CASCADE, related_name='CustomerUser')
    first_name = models.CharField(max_length=100, verbose_name='نام')
    last_name = models.CharField(max_length=100, verbose_name='نام خانوادگی')
    zip_code = models.PositiveIntegerField(default=0, verbose_name='کد پستی')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'



