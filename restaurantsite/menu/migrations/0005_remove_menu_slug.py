# Generated by Django 3.2.9 on 2021-11-20 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_menu_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='slug',
        ),
    ]
