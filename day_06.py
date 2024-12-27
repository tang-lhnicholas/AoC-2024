import numpy as np

# Part One
map1 = []

with open('AoC 2024 Day 6 Input.txt') as file:
    for line in file:
        map1.append(list(line.strip()))
x = 0
y = 0
dx = -1
dy = 0
for i in range(len(map1)):
    if '^' in map1[i]:
        x = i
        y = map1[i].index('^') # Finding location of the guard
        
count = 0
while True:
    map1[x][y] = 'X'

    if x+dx == -1 or x+dx == len(map1) or y+dy == -1 or y+dy == len(map1[0]): # Stop when out of bounds
        break

    else:   
        if map1[x+dx][y+dy] == '#':
            dx, dy = dy, -dx # Turn clockwise 90º if obstacle in front

        x += dx
        y += dy
        map1[x][y] = '^'

for line in map1: # Counting the X's
    for pos in line:
        if pos == 'X': count += 1
print(count)


# Part Two
map1 = []

with open('AoC 2024 Day 6 Input.txt') as file:
    for line in file:
        map1.append(list(line.strip()))

count2 = 0

for i in range(len(map1)):
    if '^' in map1[i]:
        x0 = i
        y0 = map1[i].index('^') # Finding initial location of the guard
          
for a in range(len(map1)):
    for b in range(len(map1[0])):
        loc_dir_hist = set([]) # A list of historic x-y-dx-dy's
        n = 0
        if map1[a][b] == '.': map1[a][b] = 'O' # Put an obstacle
        else: continue
        
        x = x0
        y = y0
        dx = -1
        dy = 0

        for i in range(len(map1)):
            if '^' in map1[i]:
                x = i
                y = map1[i].index('^') # Finding initial location of the guard

        while True:
            if x+dx == -1 or x+dx == len(map1) or y+dy == -1 or y+dy == len(map1[0]): # Stop when out of bounds
                if map1[a][b] == 'O': map1[a][b] = '.'
                break

            else:
                try:
                    while map1[x+dx][y+dy] == '#' or map1[x+dx][y+dy] == 'O':
                        dx, dy = dy, -dx # Turn clockwise 90º if obstacle in front
                except: break
                        
            if (x, y, dx, dy) in loc_dir_hist and n != 0: # If guard ends up at a same location with same dir it is an inf loop, make sure check is not the 0th step => n!=0
                count2 += 1
                if map1[a][b] == 'O': map1[a][b] = '.'
                break

            loc_dir_hist.add((x, y, dx, dy))

            x += dx
            y += dy
            n += 1
print(count2)


