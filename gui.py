import pygame
from solve_funcs import *
import numpy as np
from math import sqrt

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Puzzle Panel")
pygame.display.set_icon(pygame.image.load("Puzzle_Panel.png"))


class Tile:
    def __init__(self, x, y, state):
        self.x = x
        self.y = y
        self.color = Tile.default
        self.clicked = False
        self.rect = None
        self.state = state

    default = (194, 147, 60)
    pressed = (99, 186, 86)
    highlight = (230, 123, 62)

    def draw(self):

        self.rect = pygame.draw.rect(screen, self.color, (100*(self.x+1), 100*(self.y+1), 100, 100))  # fill
        pygame.draw.rect(screen, (0, 0, 0), (100*(self.x+1)-2, 100*(self.y+1)-2, 104, 104), 4)  # border

        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                if self.color == Tile.default:
                    self.color = Tile.pressed
                    self.state = 1
                else:
                    self.color = Tile.default
                    self.state = 0

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

    @classmethod
    def grid(cls, n):
        res = []
        for i in range(n):
            for j in range(n):
                res += [cls(j, i, 0)]
        return res

    @staticmethod
    def drawgrid(grid):
        for i in grid:
            i.draw()

    @staticmethod
    def getstates(grid):
        return [i.state for i in grid]

    @staticmethod
    def reset(grid):
        for i in grid:
            i.state = 0
            i.color = Tile.default


grid6 = Tile.grid(6)
grid5 = Tile.grid(5)
grid4 = Tile.grid(4)

currentgrid = grid6


def solvepos(gridstates):
    a = np.array(gridstates)
    b = np.reshape(a, (-1, int(sqrt(len(gridstates))))).tolist()
    c = solve(b)
    flat_c = [item for sublist in c for item in sublist]
    occurs = [i for i, x in enumerate(flat_c) if x == 1]
    return occurs


run = True
# game loop
while run:

    # fill
    screen.fill((241, 230, 136))

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_4:
                currentgrid = grid4
            if event.key == pygame.K_5:
                currentgrid = grid5
            if event.key == pygame.K_6:
                currentgrid = grid6
            if event.key == pygame.K_r:
                Tile.reset(currentgrid)
            if event.key == pygame.K_s:
                for i in solvepos(Tile.getstates(currentgrid)):
                    currentgrid[i].color = Tile.highlight

    Tile.drawgrid(currentgrid)

    pygame.display.update()
