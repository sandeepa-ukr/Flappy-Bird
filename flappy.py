import pygame as pg
from pygame.locals import *


width= 600
height= 600
speed= 20
run= True

pg.init()
pg.mixer.init()
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == KEYDOWN:
            if event.key == K_SPACE or event.key == K_UP:
                bird.bump()
                # pygame.mixer
    keys= pg.key.get_pressed()