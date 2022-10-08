import requests

api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlMjc1YWQwNjcxZDE5MjUzMjhiMTFlYmYzODQxMTkzOCIsInN1YiI6IjYzM2FhOTNhODdmM2YyMDA3ZjJlZThhYyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.EucE7jox0-pbyvtli-RlXsAyaRPJmZjltWBBQI2-xV0"

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_movies(how_many):
    data = get_popular_movies()
    return data["results"][:how_many]

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def movie_id(id):
    data = get_popular_movies()
    mamam =  data["results"]
    for film in mamam:
        if film['id'] == id:
            return film['id']

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_single_movie_cast(movie_id,ile):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"][:ile]
