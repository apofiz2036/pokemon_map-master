# Generated by Django 3.1.14 on 2024-08-05 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0010_auto_20240805_2105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemon',
            name='evolution',
        ),
        migrations.AddField(
            model_name='pokemon',
            name='prev_evolution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next_evolutions', to='pokemon_entities.pokemon', verbose_name='Эволюция'),
        ),
    ]
