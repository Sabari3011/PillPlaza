# Generated by Django 4.2.4 on 2023-09-17 02:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_prescriptivecart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prescriptivecart',
            old_name='image',
            new_name='PrescriptionImage',
        ),
    ]
