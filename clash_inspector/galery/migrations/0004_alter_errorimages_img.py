# Generated by Django 5.0.3 on 2024-04-14 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galery', '0003_errorimages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='errorimages',
            name='img',
            field=models.ImageField(height_field=10, upload_to='error/', width_field=10),
        ),
    ]
