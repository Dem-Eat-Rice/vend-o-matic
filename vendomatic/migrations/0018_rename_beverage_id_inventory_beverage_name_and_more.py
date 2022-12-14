# Generated by Django 4.1 on 2022-09-05 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendomatic', '0017_rename_beverage_name_inventory_beverage_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventory',
            old_name='beverage_id',
            new_name='beverage_name',
        ),
        migrations.RemoveField(
            model_name='beverage',
            name='type',
        ),
        migrations.AddField(
            model_name='beverage',
            name='inventory_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendomatic.inventory'),
        ),
        migrations.AlterField(
            model_name='beverage',
            name='name',
            field=models.CharField(choices=[('SODA', 'Soda'), ('WATER', 'Water'), ('JUICE', 'Juice')], default='SODA', max_length=5),
        ),
    ]
