# Generated by Django 3.2.7 on 2021-09-20 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('members', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
                ('final_amount', models.IntegerField(blank=True, null=True)),
                ('status', models.IntegerField(choices=[(1, 'ready'), (2, 'sent'), (3, 'delivered')])),
                ('address', models.TextField(blank=True, default='', null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='members.customer')),
                ('product', models.ManyToManyField(null=True, to='products.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount_percent', models.PositiveSmallIntegerField()),
                ('coupon_number', models.PositiveIntegerField()),
                ('customers', models.ManyToManyField(to='members.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
                ('final_amount', models.IntegerField(blank=True, null=True)),
                ('status', models.IntegerField(choices=[(1, 'ready'), (2, 'sent'), (3, 'delivered')])),
                ('address', models.TextField()),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='members.customer')),
                ('product', models.ManyToManyField(null=True, to='products.Product')),
            ],
        ),
    ]
