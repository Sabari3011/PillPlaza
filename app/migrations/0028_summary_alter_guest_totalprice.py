# Generated by Django 4.2.4 on 2023-09-25 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_guest_agree'),
    ]

    operations = [
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalcategory', models.IntegerField(default=0)),
                ('totalproducts', models.IntegerField(default=0)),
                ('totalsales', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='guest',
            name='totalprice',
            field=models.IntegerField(default=10),
        ),
    ]
