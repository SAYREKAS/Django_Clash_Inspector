# Generated by Django 5.0.3 on 2024-04-14 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galery', '0006_errorimages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='errorimages',
            name='img',
            field=models.ImageField(upload_to='error/'),
        ),
    ]
