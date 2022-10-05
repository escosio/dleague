import imp
from center_of_the_football_universe import get_home_team
import unittest

class TestCase(unittest.TestCase):

    def test_home_game(self):
        self.assertEqual(get_home_team("New York Jets",1), "New York Jets")
    
    def test_away_game(self):
        self.assertEqual(get_home_team("Miami Dolphins",4),"Cincinnati Bengals")

    def test_london_game(self):
        self.assertEqual(get_home_team("Green Bay Packers",5),"London")
    
    def test_mexico(self):
        self.assertEqual(get_home_team("San Francisco 49ers",11), "Mexico City")

    def test_germany(self):
        self.assertEqual(get_home_team("Tampa Bay Buccaneers",10),"Munich")

# python -m unittest tests.py