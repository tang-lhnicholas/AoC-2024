
data = []

with open('AoC 2024 Day 9 Input.txt') as file:
    disk_map = file.read()

ID = 0
for i in range(len(disk_map)):
    if not i%2: # For digits at even positions
        for n in range(int(disk_map[i])): data.append(ID)
        ID += 1
    else:
        for n in range(int(disk_map[i])): data.append('.')

# Part One
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

