# Generated by Django 4.1 on 2022-11-09 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0020_comment_item_comments_comment_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(max_length=50),
        ),
    ]