# Generated by Django 4.1 on 2022-09-03 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendomatic', '0009_remove_vendingmachine_coin_count_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendingmachine',
            name='coin',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
