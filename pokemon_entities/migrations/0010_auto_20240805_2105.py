# Generated by Django 3.1.14 on 2024-08-05 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0009_auto_20240805_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='name_en',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Английское название покемона'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='name_jp',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Японское название покемона'),
        ),
    ]