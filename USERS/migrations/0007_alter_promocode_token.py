# Generated by Django 4.1 on 2022-10-13 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('USERS', '0006_alter_promocode_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promocode',
            name='token',
            field=models.CharField(max_length=20),
        ),
    ]