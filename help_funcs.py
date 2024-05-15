import random

import game
import globals
from groups import *
from globals import player
from Alien import Alien
from Obstacle import Obstacle
from AlienBullet import AlienBullet


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


def create_obstacles():
    if globals.level == 2:
        for i in range(8):
            x = 120 + 150 * i
            y = 700
            ob1 = Obstacle(x, y)
            obstacles_group.add(ob1)
        return

    for i in range(5):
        x = 120 + 244 * i
        y = 700

        ob1 = Obstacle(x, y)
        ob2 = Obstacle(x, y - 30)
        ob3 = Obstacle(x + 30, y - 30)
        ob4 = Obstacle(x + 60, y - 30)
        ob5 = Obstacle(x + 60, y)
        obstacles_group.add(ob1)
        obstacles_group.add(ob2)
        obstacles_group.add(ob3)
        obstacles_group.add(ob4)
        obstacles_group.add(ob5)


def alien_shooting(count, n=-1):
    if n == -1:
        n = random.randint(min(count, 70), 100)
    if len(alien_group) > 0 and n == 100:
        alien = random.choice(alien_group.sprites())
        alien_bullet = AlienBullet(alien.rect.centerx, alien.rect.bottom, alien.kind)
        alien_bullet_group.add(alien_bullet)


def print_text(text, size, x, y, color=(255, 255, 255)):
    f = pg.font.Font('fonts/PIXY.ttf', size)
    text = f.render(text, True, color)
    screen.blit(text, (x, y))


def print_text_to_center(text, size, y, color=(255, 255, 255), back=False):
    f = pg.font.Font('fonts/PIXY.ttf', size)
    text = f.render(text, True, color)
    rect = text.get_rect()
    rect.center = (screen.get_width() / 2, y)
    if back:
        pg.draw.rect(screen, (0, 0, 0), rect)
    screen.blit(text, rect.topleft)


def draw_ui():
    print_text('SCORE', 40, 50, 25)
    print_text(str(globals.score), 40, 185, 25, (31, 209, 37))

    f = open('record.txt')
    bests = list(map(int, f.readlines()))
    f.close()

    if bests[globals.level] > 0:
        print_text('BEST', 40, 350, 25, (255, 255, 0))
        print_text(str(bests[globals.level]), 40, 460, 25, (255, 255, 0))

    print_text('LIVES', 40, 800, 25)

    for i in range(player.hp):
        image = pg.image.load("sprites/player.png")
        screen.blit(image, (930 + 100 * i, 23))


def check_player():
    if player.isKilled and player.hp == 0:
        game.game_over()


def check_records():
    f = open('record.txt')
    bests = list(map(int, f.readlines()))
    f.close()

    current = bests[globals.level]
    if current < globals.score:
        bests[globals.level] = globals.score

        f = open('record.txt', 'w')
        for i in range(3):
            f.write(str(bests[i]) + '\n')
        f.close()


def update_and_draw_groups():
    player.update()
    bullet_group.update()
    alien_group.update()
    alien_bullet_group.update()
    obstacles_group.update()

    if len(alien_group) == 0 and not player.isKilled:
        create_aliens()
        player.hp = min(player.hp + 1, 3)

    player_group.draw(screen)
    bullet_group.draw(screen)
    alien_group.draw(screen)
    alien_bullet_group.draw(screen)
    obstacles_group.draw(screen)


def clear_groups():
    bullet_group.empty()
    alien_group.empty()
    obstacles_group.empty()
    alien_bullet_group.empty()

    globals.score = 0
