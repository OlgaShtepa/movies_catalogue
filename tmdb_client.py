import requests
import collections

API_KEY = '57cf65f6fbb2acf8c663b6f1b3942797'
API_BASE_URL = 'https://api.themoviedb.org/3'

Movie = collections.namedtuple('Movie', 'id, title, overview, poster_path, vote_average, release_date')


def search(search_query):
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1N2NmNjVmNmZiYjJhY2Y4YzY2M2I2ZjFiMzk0Mjc5NyIsInN1YiI6IjYzZTNhNWYyMTI4M2U5MDA4ZTQ4N2E5YiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.a0GZEyPv7VTF9GimLwQGZeRFK2da-x5lWPxFszJnrMU"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    endpoint = f"{API_BASE_URL}/search/movie/?query={search_query}"

    response = requests.get(endpoint, headers=headers)
    response = response.json()
    results = response.get('results', [])
    if not results:
        return None
    return results


def get_movies(how_many, list_type):
    endpoint = f"{API_BASE_URL}/movie/{list_type}"
    params = {"api_key": API_KEY, "language": "en-US", "page": 1}
    response = requests.get(endpoint, params=params)
    response.raise_for_status()
    movies = response.json()["results"][:how_many]
    return movies


def get_single_movie(movie_id):
    endpoint = f"{API_BASE_URL}/movie/{movie_id}"
    params = {"api_key": API_KEY, "language": "en-US"}
    response = requests.get(endpoint, params=params)
    response.raise_for_status()
    movie = response.json()
    return movie


def get_single_movie_cast(movie_id):
    endpoint = f"{API_BASE_URL}/movie/{movie_id}/credits"
    params = {"api_key": API_KEY, "language": "en-US"}
    response = requests.get(endpoint, params=params)
    response.raise_for_status()
    cast = response.json()["cast"][:4]
    return cast


def get_movie_images(movie_id):
    endpoint = f"{API_BASE_URL}/movie/{movie_id}/images"
    params = {"api_key": API_KEY}
    response = requests.get(endpoint, params=params)
    response.raise_for_status()
    images = response.json()
    return images


def get_poster_url(poster_path, size='w342'):
    return f"https://image.tmdb.org/t/p/{size}/{poster_path}"

