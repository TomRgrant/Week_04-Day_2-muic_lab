from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

# album_repository.delete_all()
# artist_repository.delete_all()

artist1 = Artist("George Ezra")
artist_repository.save(artist1)
artist2 = Artist("Panic At The Disco")
artist_repository.save(artist2)

album1 = Album("Wanted On Voyage", "Pop", artist1)
album_repository.save(album1)
album2 = Album("Death Of A Batchelor", "Idk", artist2)
album_repository.save(album2)

breakpoint()