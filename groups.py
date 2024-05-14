import pygame as pg


screen = pg.display.set_mode((1280, 800))
clock = pg.time.Clock()

player_group = pg.sprite.Group()
bullet_group = pg.sprite.Group()
alien_group = pg.sprite.Group()
alien_bullet_group = pg.sprite.Group()
obstacles_group = pg.sprite.Group()