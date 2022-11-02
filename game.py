import random

import pygame as pg
import sys

import man
from bird import Bird
from shot import Shot
from deadHolder import DeadHolder
from checkHolder import CheckHolder
from heartHolder import HeartHolder
from man import Man

pg.init()

WIDTH = 1200
HEIGHT = 800
screen = pg.display.set_mode((WIDTH, HEIGHT))

speed = 20

pressed = False

# IMAGE
sprites_list = [pg.image.load(f"sprites/stickman/stand/stand-{i}.png") for i in range(1, 6)]
sprites_walk_l_list = [pg.image.load(f"sprites/stickman/walk-left/walk-{i}.png") for i in range(1, 6)]
sprites_walk_r_list = [pg.image.load(f"sprites/stickman/walk-right/walk-{i}.png") for i in range(1, 6)]
bird_left_list = [pg.image.load("sprites/bird/bird-left/bird-left-1.png"), pg.image.load("sprites/bird/bird-left/bird-left-2.png")]
bird_right_list = [pg.image.load("sprites/bird/bird-right/bird-right-1.png"), pg.image.load("sprites/bird/bird-right/bird-right-2.png")]
bullet_img_list = [pg.image.load(f"sprites/bullet/bullet_{i}.png") for i in range(1, 5)]
heart_img = pg.image.load("sprites/heart/heart.png")

bird_list_img = bird_left_list + bird_right_list
for i in range(4):
    bird_list_img[i] = pg.transform.scale(bird_list_img[i], (75, 75))
for i in range(5):
    sprites_list[i] = pg.transform.scale(sprites_list[i], (200, 200))
    sprites_walk_l_list[i] = pg.transform.scale(sprites_walk_l_list[i], (200, 200))
    sprites_walk_r_list[i] = pg.transform.scale(sprites_walk_r_list[i], (200, 200))

for i in range(4):
    bullet_img_list[i] = pg.transform.scale(bullet_img_list[i], (40, 40))

# CREATE_OBJECTS
man_obj = Man(screen, sprites_list[0], WIDTH // 2 - 100, HEIGHT // 2 - 100)
bird_list = []
bullet_list = []
random_create = random.randint(20, 60)
dH = DeadHolder()
cH = CheckHolder()
holders_list = [dH, cH]
hearts_list = [HeartHolder(heart_img, (510, 0)), HeartHolder(heart_img, (560, 0)), HeartHolder(heart_img, (610, 0))]

clock = pg.time.Clock()

j = 0
l_j = 0
r_j = 0
bird_i = 0
bird_create = 0
move_side = 'stand'
total = 0
check_bird = 0

max_bullet = 5

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            pressed = True
            if event.key == pg.K_w:
                man_obj.move_w()
            elif event.key == pg.K_d and pressed:
                move_side = 'right'
            elif event.key == pg.K_s:
                man_obj.move_s()
            elif event.key == pg.K_a and pressed:
                move_side = 'left'
            elif event.key == pg.K_LEFT and len(bullet_list) < max_bullet:
                bullet_list.append(Shot(bullet_img_list, man_obj.pos_x, man_obj.pos_y, 1))
            elif event.key == pg.K_UP and len(bullet_list) < max_bullet:
                bullet_list.append(Shot(bullet_img_list, man_obj.pos_x, man_obj.pos_y, 2))
            elif event.key == pg.K_RIGHT and len(bullet_list) < max_bullet:
                bullet_list.append(Shot(bullet_img_list, man_obj.pos_x, man_obj.pos_y, 3))
            elif event.key == pg.K_DOWN and len(bullet_list) < max_bullet:
                bullet_list.append(Shot(bullet_img_list, man_obj.pos_x, man_obj.pos_y, 4))
        if event.type == pg.KEYUP:
            pressed = False
            move_side = 'stand'
    if move_side == 'stand':
        screen.fill((255, 255, 255))
        man_obj.update(screen, sprites_list[j % 5])
    if move_side == 'left':
        screen.fill((255, 255, 255))
        man_obj.move_a()
        man_obj.update(screen, sprites_walk_l_list[l_j % 5])
    if move_side == 'right':
        screen.fill((255, 255, 255))
        man_obj.move_d()
        man_obj.update(screen, sprites_walk_r_list[r_j % 5])

    j += 1
    l_j += 1
    r_j += 1
    if j == 5:
        j = 0
    if l_j == 5:
        l_j = 0
    if r_j == 5:
        r_j = 0
    if bird_i == 2:
        bird_i = 0

    if bird_create % random_create == 0:
        bird_list.append(Bird(screen, bird_list_img[0], bird_list_img))
        random_create = random.randint(10, 30)

    for bird in bird_list[::-1]:
        for bullet in bullet_list[::-1]:
            if bullet.collision(bird):
                bird_list.remove(bird)
                bullet_list.remove(bullet)
                total += 1
                dH.set_total(total)
            if bullet.over_border:
                bullet_list.remove(bullet)
        if man_obj.check_collision(bird):
            print(1)
        bird.update(screen, bird_i)
    for bird in bird_list[::-1]:
        if bird.over_border:
            check_bird += 1
            cH.set_total(check_bird)
        if not bird.active:
            bird_list.remove(bird)
    for bullet in bullet_list:
        bullet.update(screen)

    bird_i += 1
    bird_create += 1

    for holder in holders_list:
        holder.update(screen)

    for heart in hearts_list:
        heart.update(screen)
    pg.display.flip()
    clock.tick(15)