# Generated by Django 3.2.7 on 2021-10-11 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0008_alter_basket_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_content',
            field=models.TextField(null=True, verbose_name='آدرس'),
        ),
        migrations.AlterField(
            model_name='address',
            name='title',
            field=models.CharField(max_length=500, null=True, verbose_name='عنوان آدرس'),
        ),
        migrations.AlterField(
            model_name='basket',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basket.address', verbose_name='آدرس'),
        ),
    ]
