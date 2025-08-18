from django.db import models 

from django.core.validators import MaxValueValidator, MinValueValidator

class Band(models.Model):
    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField()
    biography = models.fields.CharField()
    year_formed = models.fields.IntegerField()
    validators=[MinValueValidator(1900), MaxValueValidator(2021)]
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)


GENRE_CHOICES = [
    ('ROCK', 'Rock'),
    ('JAZZ', 'Jazz'),
    ('POP', 'Pop'),
]

class Listing(models.Model):
    genre = models.CharField(
        choices=GENRE_CHOICES,
        max_length=5,
    )






    
def __str__(self):
    return f"{self.name}"
