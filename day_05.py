rules = []
instructions = []

with open('AoC 2024 Day 5 Input.txt') as file:
    for line in file:
         if '|' in line: rules.append(line.strip().split('|'))
         elif ',' in line: instructions.append(line.strip().split(','))

# Part One
valid_inst = []
def check_ok(inst):
    ok = []
    for i in range(len(inst)):
        update = inst[i]
        for rule in rules:
            if str(rule[0]) == str(update) and str(rule[1]) in inst[:i]:
                ok.append(False)
            else: ok.append(True)
    return all(ok)

for inst in instructions:
    if check_ok(inst) == True: valid_inst.append(inst)
    
sum_valid = 0

for valid in valid_inst:
    sum_valid += int(valid[len(valid)//2])

print(sum_valid)



# Part Two
invalid_inst = []
corrected_inst = []

for inst in instructions:
    if inst not in valid_inst:
        invalid_inst.append(inst)

for invalid in invalid_inst:
    while check_ok(invalid) == False:
        for i in range(len(invalid)-1): # Linear search - swap positions for pairs that do not follow rules until the instruction is valid
            if check_ok([invalid[i], invalid[i+1]]) == False:
                invalid[i], invalid[i+1] = invalid[i+1], invalid[i]
    corrected_inst.append(invalid)

sum_corrected = 0

for corrected in corrected_inst:
    sum_corrected += int(corrected[len(corrected)//2])

print(sum_corrected)
