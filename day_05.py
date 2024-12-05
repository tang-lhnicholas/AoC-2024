text = []

with open('AoC 2024 Day 4 Input.txt') as file:
    for line in file:
        text.append('O'+line.strip()+'O') # 'O' character as buffer

text.insert(0, ['O' for i in range(len(text[0]))])
text.append(['O' for i in range(len(text[0]))])

# Part One
count = 0
for i in range(len(text)):
    for j in range(len(text[0])):
        if text[i][j] == 'X':
            try:
                if [text[i+n][j] for n in range(4)] == ['X', 'M', 'A', 'S']: count += 1 # →
            except: pass

            try:
                if [text[i+n][j+n] for n in range(4)] == ['X', 'M', 'A', 'S']: count += 1 # ↘
            except: pass

            try:
                if [text[i][j+n] for n in range(4)] == ['X', 'M', 'A', 'S']: count += 1 # ↓
            except: pass

            try:
                if [text[i-n][j+n] for n in range(4)] == ['X', 'M', 'A', 'S']: count += 1 # ↙
            except: pass

            try:
                if [text[i-n][j] for n in range(4)] == ['X', 'M', 'A', 'S']: count += 1 # ←
            except: pass

            try:
                if [text[i-n][j-n] for n in range(4)] == ['X', 'M', 'A', 'S']: count += 1 # ↖
            except: pass

            try:
                if [text[i][j-n] for n in range(4)] == ['X', 'M', 'A', 'S']: count += 1 # ↑
            except: pass
            
            try:
                if [text[i+n][j-n] for n in range(4)] == ['X', 'M', 'A', 'S']: count += 1 # ↗
            except: pass


# Part Two
count_x = 0
for i in range(len(text)):
    for j in range(len(text[0])):
        if text[i][j] == 'A':
            try:
                if [text[i-1][j-1], text[i-1][j+1], text[i+1][j-1], text[i+1][j+1]] in [['M', 'S', 'M', 'S'], ['M', 'M', 'S', 'S'], ['S', 'M', 'S', 'M'], ['S', 'S', 'M', 'M']]:
                    count_x += 1
            except: pass


print(count_x)
