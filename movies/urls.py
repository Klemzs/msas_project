from django.urls import path 
from .views import MovieListView, GenreListView, MovieSearchView, WatchMovieView

urlpatterns = [
        path('', MovieListView.as_view(), name = 'movie-list'),
        path('search/', MovieSearchView.as_view(), name = 'movie-search'),
        path('genres/', GenreListView.as_view(), name = 'genre-list'),
        path('<int:pk>/watch/', WatchMovieView.as_view(), name = 'movie-watch'),
    ]
