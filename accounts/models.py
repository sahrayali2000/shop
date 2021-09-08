from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    phone = models.CharField(max_length=30)
    image = models.FileField(upload_to='univercity/images', null=True, blank=True)
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.username



