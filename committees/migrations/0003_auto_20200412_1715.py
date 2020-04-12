# Generated by Django 3.0.5 on 2020-04-12 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('committees', '0002_committee_shortname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='person',
            name='last_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]