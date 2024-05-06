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

    def update(self):
        speed = 7

        key = pg.key.get_pressed()
        if key[pg.K_LEFT] and self.rect.left > 0:
            self.rect.x -= speed
        if key[pg.K_RIGHT] and self.rect.right < screen.get_width():
            self.rect.x += speed
        if key[pg.K_SPACE] and len(bullet_group) == 0:
            bullet = Bullet(self.rect.centerx, self.rect.top)
            bullet_group.add(bullet)


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


class Alien(pygame.sprite.Sprite):
    def __init__(self, x, y, kind):
        pygame.sprite.Sprite.__init__(self)
        self.kind = kind
        self.anim = 1
        self.image = pygame.image.load(f"sprites/alien_{self.kind}_{self.anim}.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.count = 0
        self.dir = 15

    def update(self):
        self.count += self.dir // abs(self.dir)
        if abs(self.count) >= 400:
            self.dir *= -1
            self.rect.y += 20

        elif self.count % 40 == 0:
            self.rect.x += self.dir
            self.anim *= -1
            self.image = pygame.image.load(f"sprites/alien_{self.kind}_{self.anim}.png")




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


if __name__ == '__main__':
    pg.init()
    size = 1280, 800
    screen = pg.display.set_mode(size)
    clock = pg.time.Clock()
    screen.fill('black')

    player = Player(screen.get_width() / 2, screen.get_height() - 50)

    player_group = pg.sprite.Group()
    alien_group = pg.sprite.Group()
    bullet_group = pg.sprite.Group()

    player_group.add(player)
    create_aliens()

    # # delete this
    # alien = Alien(640, 240, 0)
    # alien_group.add(alien)
    # alien = Alien(640, 300, 1)
    # alien_group.add(alien)
    # alien = Alien(640, 360, 2)
    # alien_group.add(alien)

    running = True
    while running:
        screen.fill('black')
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        player.update()
        bullet_group.update()
        alien_group.update()

        player_group.draw(screen)
        bullet_group.draw(screen)
        alien_group.draw(screen)

        pg.display.flip()
        clock.tick(60)
