# Generated by Django 4.1 on 2022-09-08 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0007_item_item_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='total_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(to='Shop.cartitem'),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.ImageField(upload_to='product_pics'),
        ),
    ]
