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
        y = map1[i].index('^')
        
count = 0
while True:
    map1[x][y] = 'X'

    if x+dx == -1 or x+dx == len(map1) or y+dy == -1 or y+dy == len(map1[0]):
        break

    else:   
        if map1[x+dx][y+dy] == '#':
            dx, dy = dy, -dx

        x += dx
        y += dy
        map1[x][y] = '^'

for line in map1:
    for pos in line:
        if pos == 'X': count += 1
print(count)
