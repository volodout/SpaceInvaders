import random
import time

import pygame as pg
import pygame.sprite
from pygame.locals import *


class Player(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.image.load("sprites/player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.hp = 3
        self.isKilled = False
        self.isCanControl = True

    def update(self):
        speed = 7

        if self.isCanControl:
            key = pg.key.get_pressed()
            if key[pg.K_LEFT] and self.rect.left > 0:
                self.rect.x -= speed
            if key[pg.K_RIGHT] and self.rect.right < screen.get_width():
                self.rect.x += speed
            if key[pg.K_SPACE] and len(bullet_group) == 0:
                bullet = Bullet(self.rect.centerx, self.rect.top)
                bullet_group.add(bullet)

        if self.isKilled and self.hp > 0:
            time.sleep(2)
            self.image = pg.image.load("sprites/player.png")
            self.rect.center = (screen.get_width() / 2, screen.get_height() - 50)
            self.isKilled = False

        if pg.sprite.spritecollide(self, alien_bullet_group, True):
            self.hp -= 1
            self.image = pg.image.load("sprites/player_death.png")
            alien_bullet_group.empty()
            self.isKilled = True
            if self.hp == 0:
                alien_group.empty()
                self.isCanControl = False


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


class Alien(pg.sprite.Sprite):
    def __init__(self, x, y, kind):
        pg.sprite.Sprite.__init__(self)
        self.kind = kind
        self.anim = 1
        self.image = pg.image.load(f"sprites/alien_{self.kind}_{self.anim}.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.count = 0
        self.dir = 15

    def update(self):
        global score
        self.count += self.dir // abs(self.dir)
        if abs(self.count) >= 420:
            self.dir *= -1
            self.rect.y += 20

        elif self.count % 42 == 0:
            self.rect.x += self.dir
            self.anim *= -1
            self.image = pg.image.load(f"sprites/alien_{self.kind}_{self.anim}.png")

        if pg.sprite.spritecollide(self, bullet_group, True):
            score += 10 + 10 * (2 - self.kind)
            self.kill()


def create_aliens():
    for row in range(5):
        for col in range(11):
            if row == 0:
                kind = 0
            elif row == 1 or row == 2:
                kind = 1
            else:
                kind = 2

            alien = Alien(240 + col * 80, 100 + row * 70, kind)
            alien_group.add(alien)


def alien_shooting(count, aliens):
    if len(aliens) > 0 and random.randint(min(count, 70), 100) == 100:
        alien = random.choice(alien_group.sprites())
        alien_bullet = AlienBullet(alien.rect.centerx, alien.rect.bottom, alien.kind)
        alien_bullet_group.add(alien_bullet)


def draw_ui():
    f1 = pg.font.Font('fonts/PIXY.ttf', 40)
    text = f1.render('SCORE', True, (255, 255, 255))
    screen.blit(text, (50, 25))

    text = f1.render(str(score), True, (31, 209, 37))
    screen.blit(text, (185, 25))

    if not player.isCanControl:
        f1 = pg.font.Font('fonts/PIXY.ttf', 120)
        if player.isKilled:
            s = 'GAME OVER'
        else:
            s = 'YOU WIN!'
        text = f1.render(s, True, (255, 255, 255))
        rect = text.get_rect()
        rect.center = (screen.get_width() / 2, screen.get_height() / 2)
        screen.blit(text, rect.topleft)
        alien_bullet_group.empty()
        return

    text = f1.render('LIVES', True, (255, 255, 255))
    screen.blit(text, (800, 25))

    for i in range(player.hp):
        image = pg.image.load("sprites/player.png")
        screen.blit(image, (930 + 100 * i, 23))


if __name__ == '__main__':
    pg.init()
    size = 1280, 800
    screen = pg.display.set_mode(size)
    clock = pg.time.Clock()
    screen.fill('black')

    player = Player(screen.get_width() / 2, screen.get_height() - 50)

    player_group = pg.sprite.Group()
    bullet_group = pg.sprite.Group()
    alien_group = pg.sprite.Group()
    alien_bullet_group = pg.sprite.Group()

    player_group.add(player)
    create_aliens()

    shooting_count = 0
    score = 0
    running = True
    while running:
        screen.fill('black')

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        alien_shooting(shooting_count // 300, alien_group)
        shooting_count += 1

        player.update()
        bullet_group.update()
        alien_group.update()
        alien_bullet_group.update()

        if len(alien_group) == 0:
            player.isCanControl = False

        player_group.draw(screen)
        bullet_group.draw(screen)
        alien_group.draw(screen)
        alien_bullet_group.draw(screen)

        draw_ui()

        pg.display.flip()
        clock.tick(60)
