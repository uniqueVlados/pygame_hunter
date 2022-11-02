import pygame as pg
from random import randint
from gameObject import GameObject


class Bird(GameObject):
    def __init__(self, screen, img, image_list):
        if randint(0, 1) == 0:
            self.image_list = image_list[2:]
            x = 0
            y = randint(0, 600)
            self.side = 'right'
        else:
            self.image_list = image_list[:2]
            x = 1200 - 75
            y = randint(100, 600)
            self.side = 'left'
        self.speed = randint(5, 25)
        self.active = True
        self.over_border = False
        super().__init__(screen, img, x, y)

    def move_left(self):
        if self.x >= -70:
            self.x -= self.speed
        else:
            self.active = False
            self.over_border = True

    def move_right(self):
        if self.x <= 1200:
            self.x += self.speed
        else:
            self.active = False
            self.over_border = True

    def update(self, screen, frame):
        if self.side == 'left':
            self.move_left()
            screen.blit(self.image_list[frame], (self.x, self.y))
        else:
            self.move_right()
            screen.blit(self.image_list[frame], (self.x, self.y))
