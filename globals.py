import pygame.time

from Player import Player
from groups import screen

ticks = pygame.time.get_ticks()
player = Player(screen.get_width() / 2, screen.get_height() - 50)
player_speed = 7
bullets_count = 1
score = 0
difficult_aliens = 1
difficult_obstacles = 0
is_creative = False
