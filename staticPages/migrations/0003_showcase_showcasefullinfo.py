# Generated by Django 2.1.7 on 2019-03-24 21:20

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staticPages', '0002_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='showcase',
            name='showcaseFullInfo',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Полное описание '),
        ),
    ]
