# Generated by Django 3.2.18 on 2023-04-30 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20230429_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='is_active',
            field=models.BooleanField(default=False, null=True),
        ),
    ]