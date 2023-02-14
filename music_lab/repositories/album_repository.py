from db.run_sql import run_sql
from models.album import Album

def save(album):
    albums = []
    sql = """INSERT INTO albums (title, genre, artist_id)
             Values (%s, %s, %s)"""
    values = [album.title, album.genre, album.artist.id]
    results = run_sql(sql, values)
    for row in results:
        album = Album(row['title'], row['genre'], row['artist'])
        album.id = results[0]['id']
        albums.append(album)
    return albums


def select_all():
    albums = []
    sql = """SELECT * FROM albums"""
    results = run_sql(sql)
    for row in results:
        album = Album(row['title'], row['genre'], row['artist_id'], row['id'])
        albums.append(album)
    return albums


def select(id):
    sql = "SELECT * FROM albums WHERE id == %s"
    values = [id]


def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)


def delete(id):
    pass


def update():
    pass