from gameObject import GameObject


class Man(GameObject):
    def __init__(self, screen, img, pos_x, pos_y):
        super().__init__(screen, img, pos_x, pos_y)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.speed = 20

    def move_a(self):
        if self.pos_x > 0:
            self. pos_x -= self.speed

    def move_d(self):
        if self.pos_x < 1000:
            self.pos_x += self.speed

    def move_w(self):
        if self.pos_y > 0:
            self.pos_y -= self.speed

    def move_s(self):
        if self.pos_y < 600:
            self.pos_y += self.speed

    def update(self, screen, img):
        screen.blit(img, (self.pos_x, self.pos_y))