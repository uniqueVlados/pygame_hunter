import pygame as pg
from pygame.color import THECOLORS

pg.init()


class CheckHolder:
    FONT = pg.font.Font("fonts/holdersFont.ttf", 50)
    holdertext = "Пропущенные Утки:"

    def __init__(self):
        self.total = 0
        self.text = CheckHolder.FONT.render(str(self.total), True, THECOLORS["black"])
        self.holdertext = CheckHolder.FONT.render(str(self.holdertext), True, THECOLORS["black"])

    def set_total(self, total):
        self.text = CheckHolder.FONT.render(str(total), True, THECOLORS["black"])

    def update(self, screen):
        a = 440
        screen.blit(self.text, (a, 0))
        screen.blit(self.holdertext, (5, 0))
        if a >= 10:
            a += 10
        if a >= 100:
            a += 10