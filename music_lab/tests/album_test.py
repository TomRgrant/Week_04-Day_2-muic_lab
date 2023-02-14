import unittest
from models.album import Album
from models.artist import Artist


class TestAlbum(unittest.TestCase):
    def setUp(self):
        self.artist = Artist("Stone Sour")
        self.album = Album("Come What(ever) May", "Metal", self.artist)
