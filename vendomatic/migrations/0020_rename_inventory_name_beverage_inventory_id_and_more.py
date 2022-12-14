# Generated by Django 4.1 on 2022-09-05 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendomatic', '0019_alter_beverage_inventory_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='beverage',
            old_name='inventory_name',
            new_name='inventory_id',
        ),
        migrations.AlterField(
            model_name='beverage',
            name='id',
            field=models.CharField(max_length=299, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='beverage',
            name='name',
            field=models.CharField(choices=[('soda', 'SODA'), ('water', 'WATER'), ('juice', 'JUICE')], default='SODA', max_length=5),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='beverage_name',
            field=models.ForeignKey(default='SODA', null=True, on_delete=django.db.models.deletion.CASCADE, to='vendomatic.beverage'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='machine_name',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='vendomatic.vendingmachine'),
        ),
    ]
