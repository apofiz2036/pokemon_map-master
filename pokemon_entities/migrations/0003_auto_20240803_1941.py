# Generated by Django 3.1 on 2024-08-03 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0002_auto_20240803_1940'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemonentity',
            old_name='title',
            new_name='pokemon_name',
        ),
    ]
