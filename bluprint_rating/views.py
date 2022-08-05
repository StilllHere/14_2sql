from flask import Blueprint
from work_bd import search_children, search_family, search_adult
from flask import jsonify

rating_blueprint = Blueprint('rating_blueprint', __name__)

@rating_blueprint.route('/children')
def page_children():
    movie = search_children()
    return jsonify(movie)


@rating_blueprint.route('/family')
def page_family():
    movie = search_family()
    return jsonify(movie)

@rating_blueprint.route('/adult')
def page_adult():
    movie = search_adult()
    return jsonify(movie)