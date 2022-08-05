from work_bd import get_movie_by_title, get_movie_in_diapazon, page_genre
from flask import Flask, jsonify
from bluprint_rating.views import rating_blueprint

app = Flask(__name__)

app.register_blueprint(rating_blueprint, url_prefix='/rating')

@app.route('/')
def hellow():
    return "Hellowww"

@app.route("/movies/<movie_title>/")
def page_movie(movie_title):
    movie = get_movie_by_title(movie_title)
    return jsonify(movie)

@app.route("/movie/<int:year1>/to/<int:year2>")
def page_films_in_years(year1, year2):
    return jsonify(get_movie_in_diapazon(year1,year2))

@app.route("/genre/<genre>/")
def page_genres(genre):
    movie = page_genre(genre)
    return jsonify(movie)

app.run()
