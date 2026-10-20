import math
import random
import time

gridlength = 3
bombs = 1

known = []
grid = []
alive = True

def setup():
    emptys = (gridlength*gridlength) - bombs
    for i in range(emptys):
        grid.append(0)
    for i in range(bombs):
        grid.append(1)
    random.shuffle(grid)

def loop():
    print(known)

setup()
while(alive):
    loop()