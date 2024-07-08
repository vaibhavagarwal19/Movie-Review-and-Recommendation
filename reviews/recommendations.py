# reviews/recommendations.py

from .models import Movie, Review, User

def get_recommendations_for_user(user):
    liked_movies = Movie.objects.filter(reviews__user=user, reviews__rating__gte=4)
    similar_users = User.objects.filter(reviews__movie__in=liked_movies).exclude(pk=user.pk).distinct()
    recommended_movies = Movie.objects.filter(reviews__user__in=similar_users).distinct().exclude(reviews__user=user)[:10]
    return recommended_movies
