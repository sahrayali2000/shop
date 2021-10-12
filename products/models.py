from django.db import models
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200,verbose_name='عنوان')
    image = models.ImageField(upload_to='category/images', null=True, blank=True,verbose_name='تصویر')
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها '


    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200,verbose_name='نام محصول')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name='دسته بندی محصول')
    image = models.ImageField(upload_to='product/images', null=True, blank=True,verbose_name='تصویر محصول')
    discription = models.TextField(verbose_name='توضیحات')
    price = models.IntegerField(verbose_name='قیمت')
    inventory = models.IntegerField(verbose_name='موجودی محصول')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات '

