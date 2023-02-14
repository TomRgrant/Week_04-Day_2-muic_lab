import unittest
from models.album import Album
from models.artist import Artist


class TestAlbum(unittest.TestCase):
    def setUp(self):
        self.artist = Artist("Stone Sour")
        self.album = Album("Come What(ever) May", "Metal", self.artist)

    def test_has_title(self):
        expected = "Come What(ever) May"
        actual = self.title
        self.assertEqual(expected,actual)
