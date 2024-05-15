from unittest import TestCase

import pygame as pg

import groups
from help_funcs import *
from groups import *


class HelpFuncsTest(TestCase):
    def test_create_aliens(self):
        create_aliens()
        self.assertTrue(len(alien_group) > 0)

    def test_create_obstacles_easy(self):
        globals.level = 0
        create_obstacles()
        self.assertTrue(len(obstacles_group) > 0)

    def test_create_obstacles_medium(self):
        globals.level = 1
        create_obstacles()
        self.assertTrue(len(obstacles_group) > 0)

    def test_create_obstacles_hard(self):
        globals.level = 2
        create_obstacles()
        self.assertTrue(len(obstacles_group) > 0)

    def test_alien_shooting(self):
        alien_group.add(Alien(0, 0, 1))
        alien_shooting(0, 100)
        self.assertTrue(len(alien_bullet_group) > 0)

    def test_clear_groups(self):
        create_aliens()
        create_obstacles()
        alien_shooting(0, 100)
        globals.score = 1

        clear_groups()
        self.assertEqual(len(alien_group), 0)
        self.assertEqual(len(obstacles_group), 0)
        self.assertEqual(len(alien_bullet_group), 0)
        self.assertEqual(globals.score, 0)

    def test_print_text(self):
        pg.init()
        groups.screen = pg.display.set_mode((5, 5))
        scr0 = pg.image.tostring(pg.display.get_surface(), 'RGB')
        print_text('test', 1, 0, 0)
        scr1 = pg.image.tostring(pg.display.get_surface(), 'RGB')
        self.assertTrue(is_not_eq_surfaces(scr0, scr1))

    def test_print_text_to_center(self):
        pg.init()
        groups.screen = pg.display.set_mode((5, 5))
        scr0 = pg.image.tostring(pg.display.get_surface(), 'RGB')
        print_text_to_center('test', 5, 0, back=True)
        scr1 = pg.image.tostring(pg.display.get_surface(), 'RGB')
        self.assertTrue(is_not_eq_surfaces(scr0, scr1))

    def test_draw_ui(self):
        pg.init()
        groups.screen = pg.display.set_mode((200, 200))
        scr0 = pg.image.tostring(pg.display.get_surface(), 'RGB')
        draw_ui()
        scr1 = pg.image.tostring(pg.display.get_surface(), 'RGB')
        self.assertTrue(is_not_eq_surfaces(scr0, scr1))

    def test_update_and_draw_groups(self):
        pg.init()
        groups.screen = pg.display.set_mode((500, 500))
        create_aliens()
        alien_shooting(0, 100)
        player_group.add(player)

        scr0 = pg.image.tostring(pg.display.get_surface(), 'RGB')
        update_and_draw_groups()
        scr1 = pg.image.tostring(pg.display.get_surface(), 'RGB')
        self.assertTrue(is_not_eq_surfaces(scr0, scr1))


def is_not_eq_surfaces(scr0, scr1):
    for i in range(len(scr0)):
        if scr0[i] != scr1[i]:
            return True
        if i == len(scr0) - 1:
            return False
