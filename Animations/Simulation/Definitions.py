# Import modules

import numpy as np
import pygame as pg
from GAME_pygame.KeepingNasaAfloat.Animations.Simulation.Constants import *
from math import *

# Definition for distance


def distance(a, b):
    # Find distance in components
    x = b[0]-a[0]
    y = b[1]-a[1]
    # Put components in a vector
    distvec = np.array([x, y])
    return distvec


def Mdistance(a, b):
    # Find distance in components
    x = b[0]-a[0]
    y = b[1]-a[1]
    # Put components in a vector
    distM = sqrt((x**2)+(y**2))
    return distM


def Fgrav(a, b, m1, m2):
    DistM = Mdistance(a, b)   # Distance Modulus
    DistV = distance(a, b)    # Distance Vector
    F = (Grav * m1 * m2) / (DistM ** 2)
    Fx = F*(DistV[0]/DistM)
    Fy = F*(DistV[1]/DistM)
    ForceV = np.array((Fx, Fy))
    return ForceV

