# Generated by Django 3.2.9 on 2021-11-20 16:54

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_remove_menu_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='empty', editable=False, populate_from='name'),
            preserve_default=False,
        ),
    ]
