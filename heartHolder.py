import pygame as pg


class HeartHolder:

    def __init__(self, img, pos):
        self.img = pg.transform.scale(img, (50, 50))
        self.pos = pos

    def update(self, screen):
        screen.blit(self.img, self.pos)