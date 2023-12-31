# Generated by Django 4.2.4 on 2023-09-19 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_orders_orderitems'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.CharField(choices=[('Active', 1), ('Dispatched', 2), ('Out For Delivery', 3), ('Delivered', 4), ('Declined', 5)], default='Active', max_length=50),
        ),
    ]
