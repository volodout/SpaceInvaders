import pygame as pg
from globals import screen


class AlienBullet(pg.sprite.Sprite):
    def __init__(self, x, y, kind):
        super().__init__()
        self.kind = kind
        self.image = pg.image.load(f"sprites/alien_bullet_{self.kind}.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.rect.y += 7

        if self.rect.top > screen.get_height():
            self.kill()
