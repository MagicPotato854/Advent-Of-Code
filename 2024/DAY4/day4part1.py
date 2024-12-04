import numpy as np

# Read in the data
with open('DAY4/day4.txt', 'r') as data:  # Should be 18 for test4part1.txt
    data = [i.rstrip('\n') for i in data.readlines()]
    data_ls = [list(i) for i in data]

xmas = 0

# Search for horizontal XMAS's (plus reversed ones)
for line in data:
    xmas += line.count('XMAS') + line.count('SAMX')

# Search for vertical XMAS's (plus reversed ones)
rotated = np.rot90(np.array(data_ls)).tolist()
for line in rotated:
    line = ''.join(line)
    xmas += line.count('XMAS') + line.count('SAMX')

# Search for Diagonal XMAS's (plus reversed ones)
diag_str = []
diag_str.append(''.join([data_ls[i][i] for i in range(len(data_ls))]))
for i in range(1, len(data_ls)):
    diag_str.append(''.join([data_ls[j][j + i] for j in range(len(data_ls) - i)]))
    diag_str.append(''.join([data_ls[j + i][j] for j in range(len(data_ls) - i)]))
for line in diag_str:
    xmas += line.count('XMAS') + line.count('SAMX')

diag_str = []
diag_str.append(''.join([data_ls[-i - 1][i] for i in range(len(data_ls))]))
for i in range(1, len(data_ls)):
    diag_str.append(''.join([data_ls[-j - 1][j + i] for j in range(len(data_ls) - i)]))
    diag_str.append(''.join([data_ls[-j - i - 1][j] for j in range(len(data_ls) - i)]))
for line in diag_str:
    xmas += line.count('XMAS') + line.count('SAMX')

print(xmas)