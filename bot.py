# import sys
import pyautogui as py
import time
import solve_funcs
from math import sqrt

r = 5  # point similarity threshold


def find(t):
    points = [py.center(j) for j in list(py.locateAllOnScreen(t + ".png", grayscale=False, confidence=0.95))]
    result = []
    for element in points:
        add = True
        for k in result:
            if abs(k.x - element.x) < r and abs(k.y - element.y) < r:
                add = False
        if add:
            result.append(element)
    return result


# sorting a 2n x n grid
def sort_coords(lst):
    result = []
    while len(lst) != 0:
        row = []
        rowy = min([j.y for j in lst])
        copy = lst.copy()
        for j in copy:
            if abs(j.y - rowy) < r:
                row.append(j)
                lst.remove(j)
        row.sort(key=lambda x: x.x)
        result.append(row)
    return result


def flatten(lst):
    return [item for sublist in lst for item in sublist]


def unflatten(lst):  # assumes len(lst) is a square number
    n = int(sqrt(len(lst)))
    return [lst[(i*n):(i*n+n)] for i in range(n)]


time.sleep(3)  # gives you time to change the active window

while True:
    # Locate all the shroom and feather tiles
    shrooms = find("shroom")
    feathers = find("feather")

    all_tiles = flatten(sort_coords(shrooms + feathers))  # list of all tiles in reading order

    shroom_locations = []
    for tile in all_tiles:
        if tile in shrooms:
            shroom_locations.append(1)
        else:
            shroom_locations.append(0)

    top = shroom_locations[:int(len(shroom_locations) / 2)]
    bottom = shroom_locations[int(len(shroom_locations) / 2):]

    board = [(a + b) % 2 for a, b in zip(top, bottom)]
    solved = flatten(solve_funcs.solve(unflatten(board)))
    indecies = [i for i, j in enumerate(solved) if j == 1]

    # input the solution
    for i in indecies:
        p = all_tiles[i + int(len(all_tiles) / 2)]
        py.click(x=p.x/2, y=p.y/2, clicks=2, interval=0.25)
        time.sleep(1)  # buffer
    time.sleep(3)  # wait for next level

    # break
