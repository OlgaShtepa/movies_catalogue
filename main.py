from flask import Flask, render_template
import tmdb_client


app = Flask(__name__)

@app.route('/')
def homepage():
    movies = tmdb_client.get_movies(how_many=8)
    return render_template("homepage.html", movies=movies, get_poster_url=tmdb_client.get_poster_url)


@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}


@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    return render_template("homepage.html")



if __name__=="__main__":
    app.run(debug=True)
