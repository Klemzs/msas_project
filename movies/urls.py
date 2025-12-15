from django.urls import path 
from .views import MovieListVIew, GenreListView, MovieSearchView

urlpatterns = [
        path('movies/', MovieListView.as_view(), name = 'movie-list'),
        path('movies/search/', MovieSearchVIew.as_view(), name = 'movie-search'),
        path('genres/', GenreListView.as_view(), name = 'genre-list'),
    ]
