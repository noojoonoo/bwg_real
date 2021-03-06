# Generated by Django 2.0.1 on 2018-02-03 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='is_creator',
            field=models.BooleanField(default=False),
        ),
    ]
