# Generated by Django 5.1.2 on 2024-11-19 06:27

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_alter_post_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='color',
            field=colorfield.fields.ColorField(default='#FFFFFFFF', image_field=None, max_length=25, samples=None),
        ),
    ]
