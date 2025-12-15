from rest_framework import generics, permissions
from .models import Movie, Genre
from django.db.models import Q
from .serializers import MovieSerializer, GenreSerializer

class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.select_related('genre').all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.AllowAny]

class GenreListView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [permissions.AllowAny]

class MovieSearchVIew(generics.ListAPIView):
    serializer_class = MovieSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        return Movie.objects.select_related('genre').filter(
                Q(title__icontains = query) |
                Q(description__icontains = query)
        )
