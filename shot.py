import pygame as pg
from random import randint
from man import Man

class Shot:
    SPEED = 60

    def __init__(self, img_list, pos_x, pos_y, side):
        self.pos_x = pos_x + 74
        self.pos_y = pos_y + 40
        self.side = side
        self.img = img_list[self.side - 1]
        self.over_border = False

    def move_up(self):
        if self.pos_y >= -1 * Shot.SPEED:
            self.pos_y -= Shot.SPEED
        else:
            self.over_border = True

    def move_left(self):
        if self.pos_x >= -1 * Shot.SPEED:
            self.pos_x -= Shot.SPEED
        else:
            self.over_border = True

    def move_right(self):
        if self.pos_x < 1200:
            self.pos_x += Shot.SPEED
        else:
            self.over_border = True

    def move_down(self):
        if self.pos_y <= 800 + Shot.SPEED:
            self.pos_y += Shot.SPEED
        else:
            self.over_border = True

    # def move_d1(self):
    #     if self.pos_y >= -1 * Shot.SPEED:
    #         self.pos_y -= Shot.SPEED
    #         self.pos_x -= Shot.SPEED

    # def move_d2(self):
    #     if self.pos_y >= -1 * Shot.SPEED:
    #         self.pos_y -= Shot.SPEED
    #         self.pos_x += Shot.SPEED

    def move(self):
        move_side = {1: self.move_left, 2: self.move_up, 3: self.move_right, 4: self.move_down}
        move_side[self.side]()

    def collision(self, bird):
        if self.pos_x - 70 <= bird.x <= self.pos_x + 70 and self.pos_y - 70 <= bird.y <= self.pos_y + 70:
            return True
        return False

    def update(self, screen):
        self.move()
        screen.blit(self.img, (self.pos_x, self.pos_y))