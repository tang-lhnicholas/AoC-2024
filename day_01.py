left_list = []
right_list = []

with open('AoC 2024 Day 1 Input.txt') as file:
    for line in file:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)
left_list, right_list = map(sorted, [left_list, right_list])

# Part One
total_dist = 0
for i in range(len(left_list)):
    d = abs(left_list[i] - right_list[i])
    total_dist += d

print(total_dist)
    
# Part Two
similarity_score = 0
for left in left_list:
    count = 0
    for right in right_list:
        if left == right: count += 1
    similarity_score += left * count

print(similarity_score)
