import json
import sqlite3
from copy import deepcopy

con = sqlite3.connect('netflix.db', check_same_thread=False)
cur = con.cursor()

def get_movie_by_title(title: str) -> dict:
        """
        Поиск по title фильмов
        """
        sqlite_query = f"""
        SELECT title, country, release_year, listed_in, description
        FROM netflix
        where title LIKE '%{title}%'
        ORDER BY release_year DESC
        LIMIT 1
        """
        cur.execute(sqlite_query)
        data = cur.fetchone()
        print(type(data))
        show = {
                'title': data[0],
                'country': data[1],
                'release_year': data[2],
                'listed_in': data[3],
                'description': data[4]
        }
        return show

def get_movie_in_diapazon(year1, year2) -> list[dict]:
        """
        Поиск фильмов по диапазону лет выпуск
        """
        query = f"""
        SELECT title, release_year
        FROM netflix
        WHERE release_year BETWEEN {year1} AND {year2} AND type = 'Movie'
        """
        show = {}
        response = []
        cur.execute(query)
        data = cur.fetchall()
        for row in data:
                show["title"] = row[0]
                show['release_year'] = row[1]
                response.append(deepcopy(show))
        return response

def search_children():
        """
        Поиск по фильмов для детей
        """
        query = f"""
        SELECT title, rating, description
        FROM netflix
        WHERE rating == 'G'
        """
        show = {}
        response = []
        cur.execute(query)
        data = cur.fetchall()
        for row in data:
                show["title"] = row[0]
                show['rating'] = row[1]
                show['description'] = row[2]
                response.append(deepcopy(show))
        return response

def search_family():
        """
        Поиск по фильмов для семьи
        """
        query = f"""
        SELECT title, rating, description
        FROM netflix
        WHERE rating in ('G', 'PG', 'PG-13', 'R')
        """
        show = {}
        response = []
        cur.execute(query)
        data = cur.fetchall()
        for row in data:
                show["title"] = row[0]
                show['rating'] = row[1]
                show['description'] = row[2]
                response.append(deepcopy(show))
        return response

def search_adult():
        """
        Поиск по фильмов для взрослых
        """
        query = f"""
        SELECT title, rating, description
        FROM netflix
        WHERE rating in ('NC-17')
        """
        show = {}
        response = []
        cur.execute(query)
        data = cur.fetchall()
        for row in data:
                show["title"] = row[0]
                show['rating'] = row[1]
                show['description'] = row[2]
                response.append(deepcopy(show))
        return response

def page_genre(genre) -> list[dict]:
        """
        Поиск по фильмов по жанрам
        """
        query = f"""
        SELECT title, description
        FROM netflix
        WHERE listed_in LIKE '%{genre}%'
        ORDER BY release_year DESC LIMIT 10
        """
        show = {}
        response = []
        cur.execute(query)
        data = cur.fetchall()
        for row in data:
                show["title"] = row[0]
                show['description'] = row[1]
                response.append(deepcopy(show))
        return response

def actor_page(actor1, actor2):
        """
        Поиск актеров игравших вместе больше 2 раз
        """
        query = f"""
        SELECT "cast"
        FROM netflix
        WHERE "cast" LIKE '%{actor1}%' AND "cast" LIKE '%{actor2}%' 
        GROUP BY '%{actor1}%'AND '%{actor2}%' 
        """
        cur.execute(query)
        data = cur.fetchall()
        li = list(data[0])
        for i in li:
                li2 = i.split(',')
        print(li2[2:])



def list_film(type, release_year, listed_in):
        """
               Получаем список названий картин с их описаниями в JSON
               """
        query = f"""
               SELECT title, description
               FROM netflix
               WHERE type LIKE '%{type}%' AND "release_year" == {release_year} and listed_in LIKE '%{listed_in}%'
               """
        cur.execute(query)
        data = cur.fetchall()
        show = {}
        response = []
        for row in data:
                show["title"] = row[0]
                show['description'] = row[1]
                response.append(deepcopy(show))
        json_resp = json.dumps(response)
        return json_resp

# Проверкa (шаги 5, 6)
actor_page('Rose McIver','Ben Lamb')
actor_page('Jack Black','Dustin Hoffman')
print(list_film('Movie','2021','Documentaries'))
