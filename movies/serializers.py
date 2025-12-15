from rest_framework import seializers
from .models import Genre, Movie

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']

class MovieSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(read_only = True)
    genre_id = serializers.PrimaryKeyRelatedField(
            queryset = Genre.objects.all(),
            source = 'genre',
            write_only = True
    )

    class Meta:
        model = Movie
        fields = [
                'id',
                'title',
                'description',
                'release_year',
                'genre',
                'genre_id'
            ]
