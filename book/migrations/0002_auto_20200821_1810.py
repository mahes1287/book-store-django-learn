# Generated by Django 3.0.1 on 2020-08-21 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='summary',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
