from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length = 100, unique = True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    genre = models.ForeignKey(Genre, on_delete = models.PROTECT, related_name = 'movies')
    release_year = models.PositiveIntegerField()

    def __str__(self):
        return self.title
