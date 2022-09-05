# Generated by Django 4.1 on 2022-09-05 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendomatic', '0014_remove_beverage_items_remaining_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='beverage',
            old_name='type_of_beverage',
            new_name='type',
        ),
        migrations.RenameField(
            model_name='inventory',
            old_name='beverage_id',
            new_name='beverage_name',
        ),
        migrations.RenameField(
            model_name='inventory',
            old_name='machine_id',
            new_name='machine_name',
        ),
        migrations.AddField(
            model_name='beverage',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]