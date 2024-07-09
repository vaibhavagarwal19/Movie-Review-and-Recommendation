# reviews/views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import viewsets, generics, filters, permissions, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken 
from .models import Movie, Review
from .serializers import MovieSerializer, ReviewSerializer
from .services import fetch_movie_details
from .recommendations import get_recommendations_for_user
from .serializers import RegisterSerializer
from rest_framework.views import APIView



class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_queryset(self):
        # Implement logic to fetch and update movies from TMDb if needed
        # Example: Fetch movie details if not already in database
        # Replace movie_id with actual TMDb movie IDs you want to fetch
        movie_ids = [12345, 67890]  # Example movie IDs
        for movie_id in movie_ids:
            fetch_movie_details(movie_id)
        
        return Movie.objects.all()
    
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['title', 'description']
    filterset_fields = ['genre']

    @action(detail=False, methods=['post'], permission_classes=[IsAuthenticated])
    def fetch_from_tmdb(self, request):
        tmdb_id = request.data.get('tmdb_id')
        if not tmdb_id:
            return Response({'error': 'TMDb ID is required'}, status=status.HTTP_400_BAD_REQUEST)

        movie = fetch_movie_details(tmdb_id)
        if movie:
            return Response(MovieSerializer(movie).data, status=status.HTTP_201_CREATED)
        return Response({'error': 'Failed to fetch movie details'}, status=status.HTTP_400_BAD_REQUEST)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['comment', 'user__username', 'movie__title']
    filterset_fields = ['rating']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RecommendationView(generics.ListAPIView):
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return get_recommendations_for_user(user)


from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def dtf_view(request):
    return Response("movie")


from .serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({"detail": "Successfully logged out."}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
   