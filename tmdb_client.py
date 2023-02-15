import requests

API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1N2NmNjVmNmZiYjJhY2Y4YzY2M2I2ZjFiMzk0Mjc5NyIsInN1YiI6IjYzZTNhNWYyMTI4M2U5MDA4ZTQ4N2E5YiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.a0GZEyPv7VTF9GimLwQGZeRFK2da-x5lWPxFszJnrMU"
headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"]


def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_movies(how_many):
    data = get_popular_movies()
    if "results" in data:
        return data["results"][:how_many]
    else:
        return []

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_movie_details(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_TOKEN}"
    response = requests.get(endpoint, headers=headers)
    return response.json()


