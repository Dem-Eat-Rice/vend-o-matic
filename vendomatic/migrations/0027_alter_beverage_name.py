# Generated by Django 4.1 on 2022-09-05 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendomatic', '0026_beverage_inventory_id_inventory_beverage_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beverage',
            name='name',
            field=models.CharField(blank=True, choices=[('soda', 'SODA'), ('water', 'WATER'), ('juice', 'JUICE')], max_length=5, null=True),
        ),
    ]
