from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
    category = models.ForeignKey(Genre, on_delete = models.SET_NULL, null = True)
    release_year = models.IntegerField()

    def __str__(self):
        return self.title
