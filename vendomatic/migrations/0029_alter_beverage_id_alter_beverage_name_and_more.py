# Generated by Django 4.1 on 2022-09-05 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendomatic', '0028_beverageinventory_alter_beverage_inventory_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beverage',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='beverage',
            name='name',
            field=models.CharField(blank=True, choices=[('SODA', 'SODA'), ('WATER', 'WATER'), ('JUICE', 'JUICE')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]