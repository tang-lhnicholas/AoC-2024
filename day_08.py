map1 = []

total = 0
with open('AoC 2024 Day 8 Input.txt') as file:
    for line in file:
        map1.append(line.strip())

ant_map = [[0 for i in range(len(map1[0]))] for j in range(len(map1))]

for i in range(len(map1)):
    for j in range(len(map1[0])):
        char1 = map1[i][j]
        for i2 in range(len(map1)):
            for j2 in range(len(map1[0])):
                char2 = map1[i2][j2]
                if char1 != '.' and char1 == char2 and [i, j] != [i2, j2]:
                    #print(char1, i, j, char2, i2, j2)
                    di = abs(i2-i)
                    dj = abs(j2-j)
                    if [i+di, j+dj] == [i2, j2]:
                        try:
                            if i-di >= 0 and j-dj >= 0:
                                ant_map[i-di][j-dj] = '#'
                        except: pass
                    elif [i-di, j-dj] == [i2, j2]:
                        try:
                            if i+di >= 0 and j+dj >= 0:
                                ant_map[i+di][j+dj] = '#'
                        except: pass
                    elif [i+di, j-dj] == [i2, j2]:
                        try:
                            if i-di >= 0 and j+dj >= 0:
                                ant_map[i-di][j+dj] = '#'
                        except: pass
                    elif [i-di, j+dj] == [i2, j2]:
                        try:
                            if i+di >= 0 and j-dj >= 0:
                                ant_map[i+di][j-dj] = '#'
                        except: pass
                        
for line in ant_map:
    for char in line:
        if char == '#':
            total += 1

print(total)



