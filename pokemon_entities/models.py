from django.db import models  # noqa F401

class Pokemon(models.Model):
    title = models.TextField()

    def __str__(self):
        return self.title