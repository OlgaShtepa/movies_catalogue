from django.core.checks import templates
from flask import Flask, render_template, request, redirect, url_for
import tmdb_client
import random


app = Flask(__name__, template_folder="templates")


@app.route('/')
def homepage():
    list_type = request.args.get('list_type', 'popular')
    movies = tmdb_client.get_movies(how_many=8, list_type=list_type)
    return render_template('homepage.html', movies=movies, current_list='popular')


@app.route('/now_playing')
def now_playing():
    movies = tmdb_client.get_movies(how_many=8, list_type='now_playing')
    return render_template('homepage.html', movies=movies, current_list='now_playing')


@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}


@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    details = tmdb_client.get_single_movie(movie_id)
    cast = tmdb_client.get_single_movie_cast(movie_id)
    movie_images = tmdb_client.get_movie_images(movie_id)
    selected_backdrop = random.choice(movie_images['backdrops'])
    return render_template("movie_details.html", movie=details, cast=cast, selected_backdrop=selected_backdrop)


@app.route('/search')
def search():
    search_query = request.args.get('q', '')
    if not search_query:
        return redirect(url_for('homepage'))
    movie = tmdb_client.search(search_query)
    if not movie:
        return render_template("no_results.html", search_query=search_query)
    return redirect(url_for('movie_details', movie_id=movie.id))



if __name__ == "__main__":
    app.run(debug=True)
