# Generated by Django 3.1 on 2020-09-18 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20200821_1352'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='title',
            new_name='address',
        ),
    ]