# Generated by Django 3.1.2 on 2020-10-19 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('committees', '0021_auto_20201017_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='committeepage',
            name='sign_up_embed_code',
            field=models.TextField(blank=True, null=True),
        ),
    ]