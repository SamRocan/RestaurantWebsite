# Generated by Django 3.2.9 on 2021-11-20 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_remove_menu_displayimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='displayImage',
            field=models.ImageField(default='menu/default.jpg', upload_to='menu/'),
        ),
    ]
