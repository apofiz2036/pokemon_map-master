# Generated by Django 3.1.14 on 2024-08-05 02:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0007_auto_20240805_0732'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemonentity',
            old_name='pokemon_name',
            new_name='name_ru',
        ),
    ]
