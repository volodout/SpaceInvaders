import pygame.time

from Bullet import Bullet
from groups import *
import globals


class Player(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.image.load("sprites/player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.hp = 3
        self.isKilled = False

    def update(self):
        if not self.isKilled:
            key = pg.key.get_pressed()
            if key[pg.K_LEFT] and self.rect.left > 50:
                self.rect.x -= globals.player_speed
            if key[pg.K_RIGHT] and self.rect.right < screen.get_width() - 50:
                self.rect.x += globals.player_speed
            if (key[pg.K_SPACE] or key[pg.K_UP]) and len(bullet_group) <= globals.bullets_count - 1:
                if pygame.time.get_ticks() - globals.ticks > 50 * globals.bullets_count:
                    globals.ticks = pygame.time.get_ticks()
                    bullet = Bullet(self.rect.centerx, self.rect.top)
                    bullet_group.add(bullet)

        if self.isKilled and self.hp > 0:
            pg.time.wait(1000)
            self.image = (pg.image.load("sprites/player.png"))
            self.rect.center = (screen.get_width() / 2, screen.get_height() - 50)
            self.isKilled = False

        if pg.sprite.spritecollide(self, alien_bullet_group, True):
            self.hp -= 1
            self.image = pg.image.load("sprites/player_death.png")
            alien_bullet_group.empty()
            self.isKilled = True
            if self.hp == 0:
                alien_group.empty()
                self.isKilled = True
