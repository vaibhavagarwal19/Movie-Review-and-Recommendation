# reviews/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, ReviewViewSet, UserCreateAPIView, RecommendationView, UserLogoutAPIView,MovieListView

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('user/register/', UserCreateAPIView.as_view(), name='user-register'),
    path('user/logout/', UserLogoutAPIView.as_view(), name='user-logout'),
    path('movies/fetch_from_tmdb/', MovieViewSet.as_view({'post': 'fetch_from_tmdb'}), name='fetch-from-tmdb'),
    path('recommendations/', RecommendationView.as_view(), name='recommendations'),
    path('', include(router.urls)),
    path('docs/', include('rest_framework.urls')),  # Include API documentation,
    path('movies/', MovieListView.as_view(), name='movie-list'),


]
