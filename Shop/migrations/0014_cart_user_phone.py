# Generated by Django 4.1 on 2022-09-20 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0013_cart_agent_confirmed'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='user_phone',
            field=models.IntegerField(default=0),
        ),
    ]