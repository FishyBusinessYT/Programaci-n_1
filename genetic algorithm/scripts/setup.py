import pygame as pg
import os

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (40, 40)
pg.init()

screen = pg.display.set_mode((1000, 1000), pg.NOFRAME)
pg.display.set_caption("")

clock = pg.time.Clock()