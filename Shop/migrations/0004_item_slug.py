# Generated by Django 4.1 on 2022-09-06 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0003_item_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='slug',
            field=models.SlugField(default=True),
            preserve_default=False,
        ),
    ]
