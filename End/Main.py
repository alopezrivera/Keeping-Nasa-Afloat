import numpy as np
import pygame as pg
from math import *
from KeepingNasaAfloat.End.Constants import *

# win = pg.display.set_mode((455, 683))

def Stagrill(win):

    v_stalin = 3

    x_stalin = 0

    #Define vectors for Rocket movement

    xy_lander = np.array((0.0, 0.0))
    vxy_lander = np.array((0.0, 0.0))
    # I define acceleration inside the loop so that gravity remains constant even after thrusting

    pg.init()
    #Load IMages

    background = pg.image.load('KeepingNasaAfloat\\'
                               'End\\background.jpeg')
    background = pg.transform.scale(background, (455, 683))
    lander = pg.image.load('KeepingNasaAfloat\\'
                           'End\\lander.png')
    lander = pg.transform.scale(lander, (70, 70))
    stalin = pg.image.load('KeepingNasaAfloat\\'
                           'End\\stalin.png')
    stalin = pg.transform.scale(stalin, (70, 50))
    fire = pg.image.load('KeepingNasaAfloat\\'
                         'End\\Fire.png')
    fire = pg.transform.scale(fire, (50, 50))
    title = pg.image.load('KeepingNasaAfloat\\'
                          'End\\title.png')
    title = pg.transform.scale(title, (455, 100))
    usa = pg.image.load('KeepingNasaAfloat\\'
                        'End\\UsaFlag.png')
    usa = pg.transform.scale(usa, (50, 50))
    boom = pg.image.load('KeepingNasaAfloat\\'
                         'End\\Explosion.png')
    boom = pg.transform.scale(boom, (120, 120))
    # Rectangles
    stalinrect = stalin.get_rect()
    landerrect = lander.get_rect()

    run = True
    doa = 'alive'

    while run:

        # Event pump
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        pg.time.delay(15)

        # Physics Engine

        axy_lander = np.array((0, Gravity))

        keys = pg.key.get_pressed()  # checking pressed keys
        if keys[pg.K_SPACE]:
            axy_lander += Thrust_vector / Mass
            win.blit(fire, (xy_lander[0]+10, xy_lander[1]+40))
        if keys[pg.K_RIGHT]:
            axy_lander += acc_sides
        if keys[pg.K_LEFT]:
            axy_lander -= acc_sides

        vxy_lander += axy_lander

        if xy_lander[1] > 620 and doa == 'dead':
            vxy_lander = np.array((0.0, 0.0))
            win.blit(usa, (xy_lander[0] + 70, 600))
            pg.time.wait(200)
            pg.display.update()
            run = False
        elif xy_lander[1] > 620 and doa == 'alive':
            lander = boom
            v_stalin = 0
            pg.display.update()
            run = False

        if xy_lander[0] < 0:
            xy_lander[0] = 455
        if xy_lander[0] > 455:
            xy_lander[0] = 0

        xy_lander += vxy_lander

        if x_stalin < xy_lander[0] and (x_stalin+70) > xy_lander[0] and xy_lander[1] > 550:
            doa = 'dead'
            v_stalin = 0
            stalin = boom

        # Stalin Movement
        x_stalin += v_stalin

        if x_stalin > 385:
            v_stalin = v_stalin * -1

        if x_stalin < 0:
            v_stalin = v_stalin * -1

        win.blit(title, (0, 0))
        win.blit(lander, xy_lander)
        win.blit(stalin, (x_stalin, 630))
        pg.display.flip()
        win.blit(background, (0, 0))
        if run == False:
            pg.time.wait(2000)

# Stagrill(win)
