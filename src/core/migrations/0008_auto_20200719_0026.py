# Generated by Django 3.0.8 on 2020-07-19 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200718_0530'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='end_date',
            new_name='end_date_time',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='start_date',
            new_name='start_date_time',
        ),
        migrations.RemoveField(
            model_name='event',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='event',
            name='start_time',
        ),
    ]
