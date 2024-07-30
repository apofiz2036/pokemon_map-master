from django.db import models  # noqa F401
from django.utils import timezone


class Pokemon(models.Model):
    title = models.TextField(
        verbose_name='Название покемона'
    )
    title_en = models.TextField(
        verbose_name='Английское название покемона',
        null=True,
        blank=True
    )
    title_jp = models.TextField(
        verbose_name='Японское название покемона',
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
    evolved_from = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='previous_evolutions',
        verbose_name='Из кого эволюционирует'
    )
    evolved_to = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='next_evolutions',
        verbose_name='В кого эволюционирует'
    )

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    title = models.ForeignKey(
        Pokemon,
        on_delete=models.CASCADE,
        verbose_name='Название покемона'
    )

    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')

    appeared_at = models.DateTimeField(
        default=timezone.now,
        verbose_name='Время появления'
    )
    disappeared_at = models.DateTimeField(
        default=timezone.now,
        verbose_name="Время исчезновения"
    )

    level = models.IntegerField(default=1, verbose_name="Уровень")
    health = models.IntegerField(default=1, verbose_name="Здоровье")
    strength = models.IntegerField(default=1, verbose_name="Атака")
    defence = models.IntegerField(default=1, verbose_name="Защита")
    stamina = models.IntegerField(default=1, verbose_name="Выносливость")
