# reviews/services.py

import requests
from .models import Movie

def fetch_movie_details(movie_id):
    api_key = '0e390afdd7cd124171fe5924edf7f22d'
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}'
    response = requests.get(url)
    
    if response.status_code == 200:
        movie_data = response.json()
        tmdb_id = movie_data['id']
        
        # Check if movie already exists in database
        movie, created = Movie.objects.update_or_create(
            tmdb_id=tmdb_id,
            defaults={
                'title': movie_data['title'],
                'description': movie_data['overview'],
                'release_date': movie_data['release_date'],
                'genre': ','.join([genre['name'] for genre in movie_data['genres']]),
                'poster': f"https://image.tmdb.org/t/p/original{movie_data['poster_path']}" if movie_data['poster_path'] else ''
            }
        )
        
        return movie
    
    return None
