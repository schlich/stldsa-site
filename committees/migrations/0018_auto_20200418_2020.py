# Generated by Django 3.0.5 on 2020-04-19 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('committees', '0017_committeepage_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='committeepage',
            name='leader_name',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='committeepage',
            name='formation_type',
            field=models.CharField(choices=[('CT', 'Committee'), ('WG', 'Working Group'), ('CU', 'Caucus')], default='', max_length=2),
        ),
    ]