from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    phone = models.CharField(max_length=30, verbose_name='شماره موبایل')
    image = models.FileField(upload_to='accounts/images', null=True, blank=True ,verbose_name='تصویر')
    re_password = models.CharField(max_length=10,verbose_name='تکرار پسورد')

    def __str__(self):
        return self.username



