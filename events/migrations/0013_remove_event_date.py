# Generated by Django 3.1.8 on 2021-04-14 04:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_auto_20210413_1811'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='date',
        ),
    ]
