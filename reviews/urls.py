# reviews/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from reviews.views import MyObtainTokenPairView , RegisterView ,LogoutView
from rest_framework_simplejwt.views import TokenRefreshView 
from rest_framework import permissions

from .views import MovieViewSet, ReviewViewSet, RecommendationView,MovieListView

router = routers.DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'reviews', ReviewViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Movie Review API",
        default_version='v1',
        description="API documentation for the Movie Review and Recommendation project",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="Awesome License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
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
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),


]
