# Generated by Django 4.2.1 on 2023-07-05 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopping_cart',
            name='user_id',
        ),
        migrations.AlterField(
            model_name='shopping_cart',
            name='total_items',
            field=models.CharField(max_length=20),
        ),
    ]