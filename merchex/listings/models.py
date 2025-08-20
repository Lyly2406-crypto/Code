from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


GENRE_CHOICES = [
    ('ROCK', 'Rock'),
    ('JAZZ', 'Jazz'),
    ('POP', 'Pop'),
    ('Lydia', 'Lydia'),
]


class Band(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, choices=GENRE_CHOICES, default="Unknown")
    biography = models.TextField(blank=True, default="")
    year_formed = models.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2021)]
    )
    active = models.BooleanField(default=True)
    official_homepage = models.URLField(null=True, blank=True)


    def __str__(self):
        return self.name


class Listing(models.Model):
    genre = models.CharField(
        choices=GENRE_CHOICES,
        max_length=5,
    )

    def __str__(self):
        return f"Listing: {self.genre}"
