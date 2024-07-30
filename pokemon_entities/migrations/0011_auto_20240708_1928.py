# Generated by Django 3.1 on 2024-07-08 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0010_auto_20240708_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='description',
            field=models.TextField(verbose_name='Описание покемона'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='evolved_from',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='previous_evolutions', to='pokemon_entities.pokemon', verbose_name='Из кого эволюционирует'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='evolved_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next_evolutions', to='pokemon_entities.pokemon', verbose_name='В кого эволюционирует'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение покемона'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title',
            field=models.TextField(verbose_name='Название покемона'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_en',
            field=models.TextField(verbose_name='Английское название покемона'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_jp',
            field=models.TextField(verbose_name='Японское название покемона'),
        ),
    ]