import pygame as pg


class Bullet(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.image.load("sprites/bullet.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.rect.y -= 10

        if self.rect.bottom < 0:
            self.kill()
