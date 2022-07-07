# Generated by Django 3.2.14 on 2022-07-06 22:00

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0058_alter_newspage_related_stories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspage',
            name='related_stories',
            field=wagtail.fields.StreamField([('related_story', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock()), ('copy', wagtail.blocks.TextBlock())]))], blank=True, null=True, use_json_field=True),
        ),
    ]