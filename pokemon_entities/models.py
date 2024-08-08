from django.db import models  # noqa F401
from django.utils import timezone


class Pokemon(models.Model):
    name_ru = models.CharField(
        verbose_name='Название покемона',
        max_length=100
    )
    name_en = models.CharField(
        verbose_name='Английское название покемона',
        max_length=100,
        null=True,
        blank=True
    )
    name_jp = models.CharField(
        verbose_name='Японское название покемона',
        max_length=100,
        null=True,
        blank=True
    )
    image = models.ImageField(
        null=True,
        blank=True,
        verbose_name='Изображение покемона'
    )
    description = models.TextField(
        verbose_name='Описание покемона',
        null=True,
        blank=True
    )
    prev_evolution = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='next_evolutions',
        verbose_name='Эволюция'
    )

    def __str__(self):
        return self.name_ru


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon,
        on_delete=models.CASCADE,
        verbose_name='Название покемона'
    )

    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')

    appeared_at = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
        verbose_name='Время появления'
    )
    disappeared_at = models.DateTimeField(
        default=None,
        null=True,
        blank=True,
        verbose_name="Время исчезновения"
    )

    level = models.IntegerField(verbose_name="Уровень")
    health = models.IntegerField(verbose_name="Здоровье")
    strength = models.IntegerField(verbose_name="Атака")
    defence = models.IntegerField(verbose_name="Защита")
    stamina = models.IntegerField(verbose_name="Выносливость")