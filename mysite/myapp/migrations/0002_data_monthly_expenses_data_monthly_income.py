# Generated by Django 5.1.4 on 2024-12-25 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='monthly_expenses',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='data',
            name='monthly_income',
            field=models.IntegerField(default=0),
        ),
    ]
