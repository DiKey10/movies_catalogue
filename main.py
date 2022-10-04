from flask import Flask, render_template
#from movie import Movies
import tmdb_client

app = Flask(__name__)

@app.route('/')
def homepage():
    movies = tmdb_client.get_popular_movies()["results"][:8]
    return render_template("homepage.html", movies=movies)
"""
@app.route('/')
def homepage():
    movies = Movies().all()
    def tmdb_image_url(path):
        return tmdb_client.get_poster_url(path)
    return render_template("homepage.html", movies=movies,tmdb_image_url=tmdb_image_url)
"""

@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}


if __name__ == "__main__":
    app.run(debug=True)