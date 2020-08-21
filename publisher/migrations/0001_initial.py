# Generated by Django 3.0.1 on 2020-08-21 16:52

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address_line', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('pincode', models.CharField(max_length=200)),
                ('slug', autoslug.fields.AutoSlugField(blank=True, editable=True, null=True, populate_from='name', unique=True)),
                ('created_by', models.TextField(blank=True, null=True)),
                ('updated_by', models.TextField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
