# Generated by Django 3.1 on 2024-08-03 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemon',
            old_name='title',
            new_name='pokemon_name',
        ),
        migrations.RenameField(
            model_name='pokemon',
            old_name='title_en',
            new_name='pokemon_name_en',
        ),
        migrations.RenameField(
            model_name='pokemon',
            old_name='title_jp',
            new_name='pokemon_name_jp',
        ),
    ]