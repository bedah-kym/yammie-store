# Generated by Django 4.1 on 2022-10-12 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('USERS', '0005_alter_promocode_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promocode',
            name='token',
            field=models.CharField(default='freshi-B35L197B59', max_length=20),
        ),
    ]
