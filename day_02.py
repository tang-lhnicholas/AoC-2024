


def check_safe(l):
    all_i_or_d = all(l[i] < l[i+1] for i in range(len(l)-1)) or all(l[i] > l[i+1] for i in range(len(l)-1))  
    two_adj_lvl_req = all(1 <= abs(l[i] - l[i+1]) <= 3 for i in range(len(l)-1))
    return all_i_or_d and two_adj_lvl_req

def check_safe_problem_dampener(l):
    for i in range(1,len(l)+1):
        if check_safe(l[:i-1] + l[i:]) == True:
            return True
    return False

    
# Part One 
safe_count = 0
with open('AoC 2024 Day 2 Input.txt') as file:
    for line in file:
        l = list(map(int, line.split()))
        if check_safe(l) == True:
            safe_count += 1

print(safe_count)

# Part Two
safe_PD_count = 0
with open('AoC 2024 Day 2 Input.txt') as file:
    for line in file:
        l = list(map(int, line.split()))
        if check_safe(l) == True:
            safe_PD_count += 1
        elif check_safe_problem_dampener(l) == True:
            safe_PD_count += 1

print(safe_PD_count)

