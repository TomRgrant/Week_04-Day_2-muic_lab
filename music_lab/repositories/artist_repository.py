from db.run_sql import run_sql
from models.artist import Artist


def save(artist):
    sql = """INSERT INTO artists (name)
             Values (%s) RETURNING *"""
    values = [artist.name]
    results = run_sql(sql, values)
    artist.id = results[0]['id']
    return artist


def select_all():
    artists = []
    sql = "SELECT * FROM artists"
    results = run_sql(sql)
    for row in results:
        artist = Artist(row['name'], row['id'])
        artists.append(artist)
    return artists


def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)


def delete(id):
    pass


def update():
    pass

