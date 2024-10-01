from idlelib import testing
from unittest import TestCase

from game import *


class GameTest(TestCase):
    def test_begin(self):
        pg.init()
        begin(testing=True)
        self.assertTrue(True)

    def test_pause(self):
        pg.init()
        pause(testing=True)
        self.assertTrue(True)

    def test_menu(self):
        pg.init()
        menu(testing=True)
        self.assertTrue(True)

    def test_create_level(self):
        pg.init()
        create_level(testing=True)
        self.assertTrue(True)

    def test_game_over(self):
        pg.init()
        game_over(testing=True)
        self.assertTrue(True)