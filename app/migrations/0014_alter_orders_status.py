# Generated by Django 4.2.4 on 2023-09-19 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_orders_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Dispatched', 'Dispatched'), ('Out For Delivery', 'Out For Delivery'), ('Delivered', 'Delivered'), ('Declined', 'Declined')], default='Active', max_length=50),
        ),
    ]
