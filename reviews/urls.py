# reviews/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from drf_yasg.views import get_schema_view as get_swagger_view
from drf_yasg import openapi
from reviews.views import MyObtainTokenPairView , RegisterView ,LogoutView
from rest_framework_simplejwt.views import TokenRefreshView 

from .views import MovieViewSet, ReviewViewSet, RecommendationView,MovieListView

router = routers.DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'reviews', ReviewViewSet)

schema_view = get_swagger_view(
    openapi.Info(
        title="Movie Review and Recommendation API",
        default_version='v1',
        description="API documentation for managing movies, reviews, and providing recommendations.",
        terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="MIT License"),
    )
)

urlpatterns = [
    # path('user/register/', UserCreateAPIView.as_view(), name='user-register'),
    # path('user/logout/', UserLogoutAPIView.as_view(), name='user-logout'),
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   path('logout/', LogoutView.as_view(), name='auth_logout'),  # Logout URL
    path('register/', RegisterView.as_view(), name='auth_register'),

    path('movies/fetch_from_tmdb/', MovieViewSet.as_view({'post': 'fetch_from_tmdb'}), name='fetch-from-tmdb'),
    path('recommendations/', RecommendationView.as_view(), name='recommendations'),
    path('', include(router.urls)),
    path('docs/', include('rest_framework.urls')),  # Include API documentation,
    path('movies/', MovieListView.as_view(), name='movie-list'),


]
