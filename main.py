import pygame as pg
import random as rd
import math
from pygame.locals import *

from nmath import Vec2
from node import Node

pg.init()

# VERSIONS
# 0.1 - Setup
version = "0.1"

WIDTH = 800
HEIGHT = 400

display = pg.display.set_mode((WIDTH, HEIGHT))
dsurface = pg.Surface((WIDTH, HEIGHT), pg.SRCALPHA)

clock = pg.time.Clock()

pg.display.set_caption(f"NeuralSoup {version}")

def main():
    print("Starting")

    nodes = [ Node(10, math.pi, 20, Vec2(100, 100)) ]

    dt = 0
    tick = 0
    lastTick = 0

    while True:

        tick = pg.time.get_ticks()
        dt = (tick - lastTick) / 1000.0
        lastTick = tick
        display.fill((255, 255, 255))

        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                exit()

        for node in nodes:
            node.draw(dsurface)
            node.update()

        display.blit(dsurface, (0, 0))
        pg.display.update()

# Create some random nodes
def getNodes():
    size = 10

    nodes = [None] * size
    for i in range(size):
        nodes[i] = Node((10*rd.random())+5, (math.pi * 2 * rd.random()), int(rd.random() * 20), Vec2(WIDTH*rd.random(), HEIGHT*rd.random()))
    return nodes

if __name__ == "__main__":
    main()