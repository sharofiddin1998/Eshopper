# Generated by Django 3.1.14 on 2022-03-30 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20220330_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.IntegerField(),
        ),
    ]
