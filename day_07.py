from itertools import product

sum_of_values = 0
# Part One
with open('AoC 2024 Day 7 Input.txt') as file:
    for line in file:
        value = int(line.strip().split(':')[0])
        eq = list(map(int, line.split(':')[1].split()))

        operator_choices = ['+', '*']
        operator_combs = list(product(operator_choices, repeat=len(eq)-1))
        
        for comb in operator_combs:
            total = eq[0]
            for i in range(len(eq)-1):
                operator = comb[i]
                if operator == '+': total += eq[i+1]
                if operator == '*': total *= eq[i+1]
            if total == value:
                sum_of_values += total
                break

print(sum_of_values)


# Part Two
sum_of_values2 = 0
with open('AoC 2024 Day 7 Input.txt') as file:
    for line in file:
        value = int(line.strip().split(':')[0])
        eq = list(map(int, line.split(':')[1].split()))

        operator_choices = ['+', '*', '||']
        operator_combs = list(product(operator_choices, repeat=len(eq)-1))
        
        for comb in operator_combs:
            total = eq[0]
            for i in range(len(eq)-1):
                operator = comb[i]
                if operator == '+': total += eq[i+1]
                if operator == '*': total *= eq[i+1]
                if operator == '||': total = int(str(total) + str(eq[i+1]))
            if total == value:
                sum_of_values2 += total
                break

print(sum_of_values2)
            
        
            
        
