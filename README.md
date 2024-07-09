# Movie Review and Recommendation API

This project is a Movie Review and Recommendation API built with Django and Django REST Framework. It allows users to register, log in, and manage movie reviews. The API also integrates with The Movie Database (TMDb) API to fetch movie details and provides a recommendation system based on collaborative filtering.

## Features
1. User Authentication**: Users can register, log in, and log out via API endpoints. Only authenticated users can create, update, or delete reviews.
2. Movie Management**: Fetch movie data using TMDb API and store movie information such as title, description, release date, genre, and poster.
3. Review Management**: Users can create, read, update, and delete reviews for movies, including a rating and comment.
4. Recommendation System**: Provides movie recommendations based on collaborative filtering or a similar algorithm.
5. API Functionalities**: Searching and filtering for movies and reviews, and pagination for movie and review lists.
6. API Documentation**: Documented using Swagger/OpenAPI.
7. Postman Collection**: Includes all the API endpoints with example requests.

## Setup and Run Instructions

### Prerequisites

- Python 3.12
- Django 5.0.6
- Node.js (for frontend if any)
- TMDb API key

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/moviereview.git
   cd moviereview

2. Create a virtual environment:
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`

3. Install the required dependencies:
   pip install -r requirements.txt


4. Set up the database:
   python manage.py migrate

5. Create a superuser:
   python manage.py runserver


Environment Variables
Create a .env file in the project root and add the following environment variables:
SECRET_KEY=your_secret_key
TMDB_API_KEY=your_tmdb_api_key
DEBUG=True


Example API Requests using Postman
User Registration

POST /api/register/
Content-Type: application/json

{
  "username": "newuser",
  "password": "password123",
  "password2": "password123",
  "email": "newuser@example.com",
  "first_name": "New",
  "last_name": "User"
}

User Login
POST /api/login/
Content-Type: application/json

{
  "username": "newuser",
  "password": "password123"
}

Create a Movie
POST /api/movies/
Content-Type: application/json
Authorization: Bearer <access_token>

{
  "tmdb_id": 550,
  "title": "Fight Club",
  "description": "An insomniac office worker and a devil-may-care soapmaker form an underground fight club that evolves into something much, much more.",
  "release_date": "1999-10-15",
  "genre": "Drama",
  "poster": "https://image.tmdb.org/t/p/original/k0hslc4E7kA2Vj7y8e3l2j1k5tD.jpg"
}

Create a Review
POST /api/reviews/
Content-Type: application/json
Authorization: Bearer <access_token>

{
  "movie": 1,
  "rating": 5,
  "comment": "Great movie!"
}

Link to Postman Collection
https://github.com/vaibhavagarwal19/Movie-Review-and-Recommendation/blob/master/Movie%20Review%20API.postman_collection.json

Code Quality
Follow PEP 8 guidelines for Python code.
Ensure the code is well-documented with comments where necessary.

Swagger/OpenAPI Documentation
The API documentation is available at /swagger/. You can access it by running the server and navigating to http://127.0.0.1:8000/swagger/.
