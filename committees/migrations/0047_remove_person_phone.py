# Generated by Django 3.2.13 on 2022-07-02 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('committees', '0046_alter_committeespage_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='phone',
        ),
    ]