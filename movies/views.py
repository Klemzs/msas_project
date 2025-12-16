from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter
from django.shortcuts import get_object_or_404
from .models import Movie, Genre
from django.db.models import Q
from .permissions import IsSubscribedUser, IsAdminOrReadOnly
from .serializers import MovieSerializer, GenreSerializer

class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.select_related('genre').all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [OrderingFilter]
    ordering_fields = ['title', 'release_year']
    ordering = ['title']

class GenreListView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [permissions.AllowAny]

class MovieSearchView(generics.ListAPIView):
    serializer_class = MovieSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [OrderingFilter]
    ordering_fields = ['title', 'release_year']

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        return Movie.objects.select_related('genre').filter(
                Q(title__icontains = query) |
                Q(description__icontains = query)
        )

class WatchMovieView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsSubscribedUser]

    def get(self, request, pk):
        movie = get_object_or_404(Movie, pk = pk)

        return Response({
            "movie_id": movie.id,
            "title": movie.title,
            "stream_url": f"https://stream.msas.com/movies/{movie.id}/"
        })

class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.select_related("genre").all()
    serializer_class = MovieSerializer
    permission_classes = [IsAdminOrReadOnly]
