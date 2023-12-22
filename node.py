import pygame as pg
import math

class Node:
    COLOR = (0, 0, 0)

    # Nodes have:
    # - radius
    # - direction
    # - period
    # -! position (x, y)
    def __init__(self, radius, direction, period, position):
        self.radius = radius
        self.direction = direction
        self.period = period
        self.position = position

        self._dtick = 0

    def update(self):
        self._dtick += 1

        if self._dtick >= self.period:
            self._dtick = 0
            self.radius += 0.001
    
    def draw(self, dsurface):
        arrowLength = 20

        pg.draw.circle(dsurface, self.COLOR, (self.position.x, self.position.y), self.radius)
        pg.draw.line(dsurface, (255, 0, 0), (self.position.x, self.position.y), (self.position.x + (arrowLength * math.cos(self.direction)), self.position.y + (arrowLength * math.sin(self.direction))))
