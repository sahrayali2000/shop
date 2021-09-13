from django.db import models
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    parent = models.ForeignKey('self', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/images')
    discription = models.TextField()
    price = models.IntegerField()
    inventory = models.IntegerField()

    def __str__(self):
        return self.name
