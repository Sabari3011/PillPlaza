# Generated by Django 4.2.4 on 2023-09-23 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_alter_product_options_guest'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuestQty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField()),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product', verbose_name='name')),
            ],
        ),
        migrations.AlterField(
            model_name='guest',
            name='product',
            field=models.ManyToManyField(to='app.guestqty'),
        ),
    ]
