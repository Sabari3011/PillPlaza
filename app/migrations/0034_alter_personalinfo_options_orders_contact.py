# Generated by Django 4.2.4 on 2023-10-05 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0033_alter_personalinfo_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='personalinfo',
            options={'verbose_name': 'Personal Info', 'verbose_name_plural': 'Personal Info'},
        ),
        migrations.AddField(
            model_name='orders',
            name='contact',
            field=models.CharField(default='123', max_length=10),
        ),
    ]
