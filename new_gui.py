import solve_funcs
import wip_bot as wb
import pygame


pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Puzzle Panel")
pygame.display.set_icon(pygame.image.load("Puzzle_Panel.png"))


class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = Tile.default
        
    default = (194, 147, 60)
    highlight = (255, 123, 62)
    
    def draw(self):
        pygame.draw.rect(screen, self.color, (100 * (self.x + 1), 100 * (self.y + 1), 100, 100))  # fill
        pygame.draw.rect(screen, (0, 0, 0), (100 * (self.x + 1) - 2, 100 * (self.y + 1) - 2, 104, 104), 4)  # border


def makegrid(n):
    res = []
    for i in range(n):
        for j in range(n):
            res += [Tile(j, i)]
    return res


grid4 = makegrid(4)
grid5 = makegrid(5)
grid6 = makegrid(6)


def drawgrid(grid):
    for i in grid:
        i.draw()


def highlight(grid, inds):
    for i in inds:
        grid[i].color = Tile.highlight
        

def reset(grid):
    for i in grid:
        i.color = Tile.default


currentgrid = grid6
run = True
while run:
    # fill
    screen.fill((241, 230, 136))

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    drawgrid(currentgrid)

    # Locate all the shroom and feather tiles
    shrooms = wb.find("shroom")
    feathers = wb.find("feather")

    all_tiles = wb.flatten(wb.sort_coords(shrooms + feathers))  # list of all tiles in reading order

    shroom_locations = []
    for tile in all_tiles:
        if tile in shrooms:
            shroom_locations.append(1)
        else:
            shroom_locations.append(0)

    top = shroom_locations[:int(len(shroom_locations) / 2)]
    bottom = shroom_locations[int(len(shroom_locations) / 2):]

    if len(top) in [16, 25, 36]:
        if len(top) == 16:
            currentgrid = grid4
        elif len(top) == 25:
            currentgrid = grid5
        elif len(top) == 36:
            currentgrid = grid6

        board = [(a + b) % 2 for a, b in zip(top, bottom)]

        try:
            solved = wb.flatten(solve_funcs.solve(wb.unflatten(board)))
            indecies = [i for i, j in enumerate(solved) if j == 1]

            reset(currentgrid)
            highlight(currentgrid, indecies)
        except TypeError:
            pass

    pygame.display.update()
