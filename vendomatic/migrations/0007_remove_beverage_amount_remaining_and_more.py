# Generated by Django 4.1 on 2022-09-03 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendomatic', '0006_beverage_amount_remaining'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beverage',
            name='amount_remaining',
        ),
        migrations.AddField(
            model_name='beverage',
            name='items_remaining',
            field=models.IntegerField(default=5),
        ),
    ]
