from django.contrib.auth import get_user_model
from django.db import models
from accounts.models import User

gotten_user = get_user_model()
# Create your models here.

class Staff(models.Model):
    user = models.OneToOneField(gotten_user, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    emp_code = models.IntegerField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Customer(models.Model):
    user = models.OneToOneField(gotten_user, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    zip_code = models.PositiveIntegerField(default=0)
    discount_code = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

