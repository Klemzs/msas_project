from django.urls import path 
from .views import MovieListView, GenreListView, MovieSearchView

urlpatterns = [
        path('', MovieListView.as_view(), name = 'movie-list'),
        path('search/', MovieSearchView.as_view(), name = 'movie-search'),
        path('genres/', GenreListView.as_view(), name = 'genre-list'),
    ]
