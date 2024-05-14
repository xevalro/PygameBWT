from pygame import *
import pygame as pg
from threading import *
import threading
from time import *
import time
import os

pg.init()

# Screen Settings

bgColor = (0, 0, 0)
screen = pg.display.set_mode((640, 360))
screen.fill(bgColor)
pg.display.set_caption("Platformer")
pgRunning = True

# Variables

origin = (0,0)
scrnSize = (640, 360)

while pgRunning:

    screen.fill(bgColor)
    
    pg.display.flip()
    for event in pg.event.get();
        if event.type == pg.QUIT:
            threading.
            running = False 

