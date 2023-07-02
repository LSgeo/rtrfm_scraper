import unittest
import pytest
from rtrfm2spot import spotify_tools

class SpotifyTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def init_fixture(self):
        # can be used for stuff used throughout the tests
        # ie maybe if we mock the spotify stuff
        pass
    
    def test_spotify_dummy_test(self):
        out = spotify_tools.spotify_dummy_test(1)
        self.assertEqual(out,2)
