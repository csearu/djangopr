# Generated by Django 5.1.4 on 2024-12-25 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_rename_image_uploadedimage_original_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedimage',
            name='formatted_image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
