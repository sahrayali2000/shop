# Generated by Django 3.2.7 on 2021-10-10 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='discount_code',
        ),
    ]