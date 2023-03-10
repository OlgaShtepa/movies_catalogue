import requests

API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1N2NmNjVmNmZiYjJhY2Y4YzY2M2I2ZjFiMzk0Mjc5NyIsInN1YiI6IjYzZTNhNWYyMTI4M2U5MDA4ZTQ4N2E5YiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.a0GZEyPv7VTF9GimLwQGZeRFK2da-x5lWPxFszJnrMU"
headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}
API_KEY = "57cf65f6fbb2acf8c663b6f1b3942797"


def call_tmdb_api(endpoint):
    full_url = f"https://api.themoviedb.org/3/{endpoint}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(full_url, headers=headers)
    response.raise_for_status()
    return response.json()


def get_single_movie(movie_id):
    endpoint = f"movie/{movie_id}"
    return call_tmdb_api(endpoint)


def get_single_movie_cast(movie_id):
    endpoint = f"movie/{movie_id}/credits"
    response = call_tmdb_api(endpoint)
    return response["cast"]


def get_movies_list(list_type, page=1):
    endpoint = f"movie/{list_type}"
    params = {
        "api_key": API_KEY,
        "language": "en-US",
        "page": page
    }
    response = call_tmdb_api(endpoint)
    return response


def get_movies(list_type='popular', page=1, limit=20):
    data = get_movies_list(list_type, page=page)
    if "results" in data:
        return data["results"][:limit]
    else:
        return []


def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"


def get_movie_details(movie_id):
    endpoint = f"movie/{movie_id}"
    response = call_tmdb_api(endpoint)
    return response


def get_movie_images(movie_id):
    endpoint = f"movie/{movie_id}/images"
    response = call_tmdb_api(endpoint)
    return response


def get_popular_movies():
    endpoint = f"movie/popular"
    response = call_tmdb_api(endpoint)
    return response


def search(query):
    endpoint = f"search/movie?query={query}"
    response = call_tmdb_api(endpoint)
    return response


def get_airing_today():
    endpoint = f"tv/airing_today"
    response = call_tmdb_api(endpoint)
    return response['results']
