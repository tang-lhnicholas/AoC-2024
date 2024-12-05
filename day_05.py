rules = []
instructions = []

with open('AoC 2024 Day 5 Input.txt') as file:
    for line in file:
         if '|' in line: rules.append(line.strip().split('|'))
         elif ',' in line: instructions.append(line.strip().split(','))

# Part One
valid_instructions = []
for instruction in instructions:
    rules_satisfied = []
    for i in range(len(instruction)):
        update = instruction[i]
        for rule in rules:
            if str(rule[0]) == str(update) and str(rule[1]) in instruction[:i]:
                rules_satisfied.append(False)
            else: rules_satisfied.append(True)
    if all(rules_satisfied): valid_instructions.append(instruction)

sum1 = 0

for valid in valid_instructions:
    sum1 += int(valid[len(valid)//2])

print(sum1)






