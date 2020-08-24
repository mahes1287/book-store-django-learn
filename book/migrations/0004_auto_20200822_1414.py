# Generated by Django 3.0.1 on 2020-08-22 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_auto_20200821_2000'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='name',
            new_name='title',
        ),
        migrations.AddField(
            model_name='book',
            name='book_type',
            field=models.CharField(choices=[('EB', 'e-book'), ('PB', 'Paperback'), ('HB', 'Hardbound')], default='PB', max_length=2),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bookGenre', to='book.Genre'),
        ),
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bookLanguage', to='book.Language'),
        ),
    ]