# Generated by Django 4.0.4 on 2022-05-18 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_remove_cart_numb'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='numb',
            field=models.DecimalField(decimal_places=0, default=65, max_digits=11),
            preserve_default=False,
        ),
    ]
