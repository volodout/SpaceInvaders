from groups import *
import globals


class Obstacle(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        if globals.level == 0:
            self.image = pg.image.load("sprites/obstacle_strong.png")
        else:
            self.image = pg.image.load("sprites/obstacle_4.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.hp = 4

    def update(self):
        if pg.sprite.spritecollide(self, bullet_group, True) or pg.sprite.spritecollide(self, alien_bullet_group, True):
            if globals.level != 0:
                self.hp -= 1
                if self.hp == 0:
                    self.kill()
                    return
                self.image = pg.image.load(f"sprites/obstacle_{self.hp}.png")