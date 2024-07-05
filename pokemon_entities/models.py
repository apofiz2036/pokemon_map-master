from django.db import models  # noqa F401
from django.utils import timezone


class Pokemon(models.Model):
    title = models.TextField()
    image = models.ImageField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    title = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

    lat = models.FloatField()
    lon = models.FloatField()

    appeared_at = models.DateTimeField(default=timezone.now, verbose_name='Время появления')
    disappeared_at = models.DateTimeField(default=timezone.now, verbose_name="Время исчезновения")

    level = models.IntegerField(default=1, verbose_name="Уровень")
    health = models.IntegerField(default=1, verbose_name="Здоровье")
    strength = models.IntegerField(default=1, verbose_name="Атака")
    defence = models.IntegerField(default=1, verbose_name="Защита")
    stamina = models.IntegerField(default=1, verbose_name="Выносливость")
