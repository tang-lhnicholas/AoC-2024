
map1 = []

with open('AoC 2024 Day 8 Input.txt') as file:
    for line in file:
        map1.append(line.strip())

# Part One
anti_map = [['.' for i in range(len(map1[0]))] for j in range(len(map1))] # Map for antinodes
for i in range(len(map1)):
    for j in range(len(map1[0])):
        char1 = map1[i][j] # First antenna
        for i2 in range(len(map1)):
            for j2 in range(len(map1[0])):
                char2 = map1[i2][j2] # Second antenna
                if char1 != '.' and char1 == char2 and [i, j] != [i2, j2]:
                    # Check distance between antenna pair
                    di = abs(i2-i)
                    dj = abs(j2-j)
                    # Only add one antinode (if in bound) per antenna pair to avoid double counting
                    if [i+di, j+dj] == [i2, j2]:
                        try:
                            if i-di >= 0 and j-dj >= 0: # >= 0 requirement to avoid involving negative indexing
                                anti_map[i-di][j-dj] = '#'
                        except: pass
                    elif [i-di, j-dj] == [i2, j2]:
                        try:
                            if i+di >= 0 and j+dj >= 0:
                                anti_map[i+di][j+dj] = '#'
                        except: pass
                    elif [i+di, j-dj] == [i2, j2]:
                        try:
                            if i-di >= 0 and j+dj >= 0:
                                anti_map[i-di][j+dj] = '#'
                        except: pass
                    elif [i-di, j+dj] == [i2, j2]:
                        try:
                            if i+di >= 0 and j-dj >= 0:
                                anti_map[i+di][j-dj] = '#'
                        except: pass
total = 0                        
for line in anti_map:
    for char in line:
        if char == '#':
            total += 1

print(total)

# Part Two
anti_map2 = [['.' for i in range(len(map1[0]))] for j in range(len(map1))] # Map for antinodes
for i in range(len(map1)):
    for j in range(len(map1[0])):
        char1 = map1[i][j] # First antenna
        for i2 in range(len(map1)):
            for j2 in range(len(map1[0])):
                char2 = map1[i2][j2] # Second antenna
                if char1 != '.' and char1 == char2 and [i, j] != [i2, j2]:
                    # Check distance between antenna pair
                    di = abs(i2-i)
                    dj = abs(i2-1)

                    for x in range(len(anti_map2)): # Go through every point in anti_map to see if it is in line with 1st and 2nd antenna
                        for y in range(len(anti_map2[0])):
                            #if x!=i and x!=i2 and y!=j and y!=j2:
                            try:
                                if (x-i)/(x-i2) == (y-j)/(y-j2):
                                    anti_map2[x][y] = '#'
                            except ZeroDivisionError: pass
                            
total = 0                        
for line in anti_map2:
    for char in line:
        if char == '#':
            total += 1

print(total)
