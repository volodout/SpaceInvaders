import globals
from groups import *


class Alien(pg.sprite.Sprite):
    def __init__(self, x, y, kind):
        pg.sprite.Sprite.__init__(self)
        self.kind = kind
        self.anim = 1
        self.image = pg.image.load(f"sprites/alien_{self.kind}_{self.anim}.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.count = 0
        self.dir = 18
        self.delay = 42 - 12 * globals.level

    def update(self):
        self.count += self.dir // abs(self.dir)
        if abs(self.count) >= self.delay * 10:
            self.dir *= -1
            self.rect.y += 20

        elif self.count % self.delay == 0:
            self.rect.x += self.dir
            self.anim *= -1
            self.image = pg.image.load(f"sprites/alien_{self.kind}_{self.anim}.png")

        if pg.sprite.spritecollide(self, bullet_group, True):
            globals.score += 10 + 10 * (2 - self.kind)
            self.kill()

        if self.rect.bottom > globals.player.rect.top:
            globals.player.image = pg.image.load("sprites/player_death.png")
            alien_group.empty()
            globals.player.isKilled = True
            globals.player.hp = 0