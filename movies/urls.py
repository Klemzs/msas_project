from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieListView, GenreListView, MovieSearchView, WatchMovieView, MovieViewSet

router = DefaultRouter()
router.register(r"admin", MovieViewSet, basename = "movie-admin")

urlpatterns = [
        path('', MovieListView.as_view(), name = 'movie-list'),
        path('search/', MovieSearchView.as_view(), name = 'movie-search'),
        path('genres/', GenreListView.as_view(), name = 'genre-list'),
        path('<int:pk>/watch/', WatchMovieView.as_view(), name = 'movie-watch'),
        path('', include(router.urls)),
    ]
