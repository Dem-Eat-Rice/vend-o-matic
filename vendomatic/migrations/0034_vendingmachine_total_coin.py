# Generated by Django 4.1 on 2022-09-06 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendomatic', '0033_rename_inventory_id_beverage_inventory_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendingmachine',
            name='total_coin',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
