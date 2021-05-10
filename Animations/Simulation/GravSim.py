# Import modules

import os

from KeepingNasaAfloat.Animations.Simulation.Definitions import *

os.environ['SDL_VIDEO_CENTERED'] = '1'

pg.init()

def Grav_Sim(win):

    screen_size = (455, 683)

    background = pg.image.load('KeepingNasaAfloat\\Animations\\Simulation\\Milky Way.jpg')
    background = pg.transform.scale(background, (455, 683))
    win.blit(background, (0, 0))

    size = 1000

    earthpic = pg.image.load('KeepingNasaAfloat\\Animations\\Simulation\\Earth.png')
    earthpic = pg.transform.scale(earthpic, (size, size))
    moonpic = pg.image.load('KeepingNasaAfloat\\Animations\\Simulation\\Moon.png')
    moonpic = pg.transform.scale(moonpic, (int(size / 1.6), int(size / 1.6)))
    lunampic = pg.image.load('KeepingNasaAfloat\\Animations\\Simulation\\LunarModule.png')
    lunampic = pg.transform.scale(lunampic, (int(size / 3), int(size / 3)))
    asteroid = pg.image.load('KeepingNasaAfloat\\Animations\\Simulation\\Asteroid.png')
    asteroid = pg.transform.scale(asteroid, (int(size / 2), int(size / 2)))

    # Inputs:
    x = 200
    y = 200 - d_moon
    vx = -4500 / cf * 0.7
    vy = 300 / cf
    xy_rocket = np.array((x, y))
    vxy_rocket = np.array((vx, vy))
    axy_rocket = np.array((0, 0))

    earth_radius = 50

    # Position Vectors initial
    xy_earth = np.array((screen_size[0] / 2, screen_size[1] / 2))
    xy_earthsprite = np.array((screen_size[0] / 2 - earth_radius, screen_size[1] / 2 - earth_radius))
    xy_moon = np.array((200, 300 - d_moon))
    xy_asteroid = np.array((200.0, 450.0))

    # Velocity vectors initial
    vxy_moon = np.array((-v_moon, 0))
    vxy_asteroid = np.array((v_asteroid, 0.0))

    # Acceleration vectors Initial
    axy_moon = np.array((0, 0))
    axy_asteroid = np.array((0.0, 0.0))

    run = True

    start_time = pg.time.get_ticks()
    absolute_time = pg.time.get_ticks()

    zoom = True

    while run:

        if pg.time.get_ticks() - start_time > 20 and zoom:
            if size-size/10 < 2*earth_radius:
                zoom = False
            size = size - size / 20
            earthpic = pg.image.load('KeepingNasaAfloat\\Animations\\Simulation\\Earth.png')
            earthpic = pg.transform.scale(earthpic, (int(size), int(size)))
            moonpic = pg.image.load('KeepingNasaAfloat\\Animations\\Simulation\\Moon.png')
            moonpic = pg.transform.scale(moonpic, (int(size / 1.6), int(size / 1.6)))
            lunampic = pg.image.load('KeepingNasaAfloat\\Animations\\Simulation\\LunarModule.png')
            lunampic = pg.transform.scale(lunampic, (int(size / 3), int(size / 3)))
            asteroid = pg.image.load('KeepingNasaAfloat\\Animations\\Simulation\\Asteroid.png')
            asteroid = pg.transform.scale(asteroid, (int(size / 2), int(size / 2)))
            start_time = pg.time.get_ticks()

        # Event pump
        pg.event.pump()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        # Clock
        pg.time.delay(1)
        dt = 20

        # Moon Dynamics

        axy_moon = Fgrav(xy_moon, xy_earth, m_moon, m_earth)/m_moon

        vxy_moon += axy_moon*dt

        xy_moon += vxy_moon*dt

        # Rocket Dynamics

        axy_rocket = Fgrav(xy_rocket, xy_earth, m_rocket, m_earth)/m_rocket + \
                     Fgrav(xy_rocket, xy_moon, m_rocket, m_moon)/m_rocket

        vxy_rocket += axy_rocket*dt

        xy_rocket += vxy_rocket*dt

        # Asteroid Dynamics

        axy_asteroid = Fgrav(xy_asteroid, xy_earth, m_asteroid, m_earth)/m_asteroid + \
                       Fgrav(xy_asteroid, xy_moon, m_asteroid, m_moon)/m_asteroid

        vxy_asteroid += axy_asteroid*dt

        xy_asteroid += vxy_asteroid * dt

        # Drawing and Images

        a, b = int(xy_rocket[0]), int(xy_rocket[1])

        win.blit(background, (0, 0))

        win.blit(moonpic, xy_moon)
        win.blit(lunampic, xy_rocket)
        win.blit(asteroid, xy_asteroid)
        win.blit(earthpic, xy_earthsprite)

        absolute_dt = pg.time.get_ticks() - absolute_time

        if absolute_dt <= 5000:
            fadein_surface = pg.Surface((455, 683))
            fadein_surface.fill((0, 0, 0))
            alpha = 255 - 255 * (absolute_dt - 2000) / 3000
            fadein_surface.set_alpha(alpha)

            win.blit(fadein_surface, (0, 0))

        if absolute_dt >= 8000:
            fadeout_surface = pg.Surface((455, 683))
            fadeout_surface.fill((0, 0, 0))
            alpha = 255 * (absolute_dt-8000) / 4000
            fadeout_surface.set_alpha(alpha)

            win.blit(fadeout_surface, (0, 0))

            pg.display.update()
            pg.time.delay(25)
            if alpha >= 250:
                run = False

        pg.display.flip()

