from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.TextField()
    image = models.ImageField(null=True)

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    lat = models.FloatField()
    lan = models.FloatField()
    title = models.ForeignKey(Pokemon, on_delete=models.CASCADE)