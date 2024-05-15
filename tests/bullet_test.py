from unittest import TestCase

from Bullet import Bullet
from groups import *


class BulletTest(TestCase):
    def test_update(self):
        bullet = Bullet(2, 1)
        bullet_group.add(bullet)
        bullet.update()
        self.assertEqual(len(bullet_group), 0)