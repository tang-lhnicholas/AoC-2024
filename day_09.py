
with open('AoC 2024 Day 9 Input.txt') as file:
    disk_map = file.read()
    
# Part One
data = []
ID = 0
for i in range(len(disk_map)):
    if not i%2: # For digits at even positions
        for n in range(int(disk_map[i])): data.append(ID) # Add n ID's
        ID += 1
    else:
        for n in range(int(disk_map[i])): data.append('.') # Add n free spaces

while not ''.join(map(str, data)).isnumeric():
    if data[-1] == '.': data.pop(-1)
    else:
        data[data.index('.')] = data[-1]
        data.pop(-1)

checksum = 0
for i in range(len(data)):
    checksum += i * data[i]

print(checksum)


# Part Two
data = []
new_data = []

ID = 0
for i in range(len(disk_map)):
    if not i%2: # For digits at even positions
        data.append([ID for n in range(int(disk_map[i]))]) # Add n ID's
        ID += 1
    else:
        data.append(['.' for n in range(int(disk_map[i]))]) # Add n ID's


for i in range(ID, -1, -1):
    for x in data:
        if x != []:
            if x[0] == i:
                for y in data:
                    if y != []:
                        if y[0] == '.' and len(y) >= len(x):
                            free_space_length_to_create = len(y) - len(x)
                            y[:], x[:] = x, ['.' for n in range(len(x))]
                            data.insert(data.index(y)+1, ['.' for n in range(free_space_length_to_create)])
                            break
                        

for file in data:
    for block in file:
        if block != None:
            new_data.append(block)

checksum = 0
for i in range(len(new_data)):
    if type(new_data[i]) == int:
        checksum += i * new_data[i]

print(checksum)

