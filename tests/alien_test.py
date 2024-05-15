from unittest import TestCase

import globals
from Alien import Alien
from Bullet import Bullet
from groups import *


class AlienTest(TestCase):
    def test_go_down(self):
        alien = Alien(5, 5, 1)
        alien.count = alien.delay * 10 + 1
        y = alien.rect.y
        direction = alien.dir
        alien.update()
        self.assertTrue(y < alien.rect.y)
        self.assertTrue(direction != alien.dir)

    def test_go_sides(self):
        alien = Alien(5, 5, 1)
        image = alien.image
        x = alien.rect.x

        alien.count = 9
        alien.delay = 5
        alien.update()

        self.assertTrue(x != alien.rect.x)
        self.assertTrue(image != alien.image)

    def test_collides(self):
        alien = Alien(5, 5, 1)
        alien_group.add(alien)
        bullet = Bullet(5, 5)
        bullet_group.add(bullet)

        alien.update()
        self.assertEqual(len(alien_group), 0)
        self.assertEqual(len(bullet_group), 0)
        self.assertTrue(globals.score != 0)

    def test_lose_player(self):
        alien = Alien(5, screen.get_height() - 50, 1)
        alien_group.add(alien)
        image = globals.player.image

        alien.update()
        self.assertEqual(len(alien_group), 0)
        self.assertTrue(image != globals.player.image)
