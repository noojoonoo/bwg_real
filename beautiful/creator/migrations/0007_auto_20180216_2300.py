# Generated by Django 2.0.1 on 2018-02-16 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creator', '0006_auto_20180214_1712'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='image',
            new_name='item_image',
        ),
    ]
