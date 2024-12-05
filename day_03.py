
import re

with open('AoC 2024 Day 3 Input.txt') as file:
    text = file.read()

# Part One
muls = re.findall(r'mul\(\d{1,3},\d{1,3}\)', text)
pairs = []
total = 0
for obj in muls:
    pair = obj.replace('mul(', '').replace(')', '').split(',')
    pairs.append(pair)

for pair in pairs: total += int(pair[0])*int(pair[1])
print(total)

# Part Two

total_enabled = 0

for pair in pairs:
    index_do = text.rfind("do()", 0, text.index(f'mul({pair[0]},{pair[1]})'))
    index_dont = text.rfind("don\'t()", 0, text.index(f'mul({pair[0]},{pair[1]})'))
    if index_do > index_dont or index_dont == -1:
        total_enabled += int(pair[0])*int(pair[1])
print(total_enabled)

