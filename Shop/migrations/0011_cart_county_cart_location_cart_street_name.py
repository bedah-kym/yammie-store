# Generated by Django 4.1 on 2022-09-18 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0010_alter_cart_ref_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='county',
            field=models.CharField(default=False, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cart',
            name='location',
            field=models.CharField(default='china', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cart',
            name='street_name',
            field=models.CharField(default='sub county', max_length=100),
            preserve_default=False,
        ),
    ]
