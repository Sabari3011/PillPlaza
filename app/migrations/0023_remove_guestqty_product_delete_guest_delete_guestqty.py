# Generated by Django 4.2.4 on 2023-09-23 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_guestqty_alter_guest_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guestqty',
            name='Product',
        ),
        migrations.DeleteModel(
            name='Guest',
        ),
        migrations.DeleteModel(
            name='GuestQty',
        ),
    ]
