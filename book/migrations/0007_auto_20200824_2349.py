# Generated by Django 3.0.1 on 2020-08-24 23:49

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_auto_20200824_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=autoslug.fields.AutoSlugField(blank=True, editable=True, null=True, populate_from='title', unique=True),
        ),
    ]
