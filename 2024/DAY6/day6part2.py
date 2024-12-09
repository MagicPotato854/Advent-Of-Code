# Read in the data
with open('2024/DAY6/test6.txt', 'r') as data:
    data = [row.rstrip('\n') for row in data]

# Declare and initialize variables
orig_data = data.copy()
directs = ['^', '>', 'v', '<']
direct = None
guard = True
pos = None
past_pos = []
total = 0

# Find guard
for y, row in enumerate(data):
    print(str(y).rjust(3), row, sep=' ')
    for x, char in enumerate(row):
        if char in directs:
            pos = ((x, y), char)
            break
print(pos)

# Move the guard until it goes off screen or loops
for orig_x, orig_row in enumerate(orig_data):
    for orig_y, orig_char in enumerate(orig_row):
        if orig_char == '#':
            continue
        data[orig_y] = data[orig_y][:orig_x] + '#' + data[orig_y][orig_x + 1:]
        for y, row in enumerate(data):
            print(str(y).rjust(3), row, sep=' ')
        while True:
            x, y = pos[0]
            direct = pos[1]
            try:
                if direct == '^':
                    if data[y - 1][x] == '#':
                        direct = '>'
                        x += 1
                    else:
                        y -= 1
                elif direct == '>':
                    if data[y][x + 1] == '#':
                        direct = 'v'
                        y += 1
                    else:
                        x += 1
                elif direct == 'v':
                    if data[y + 1][x] == '#':
                        direct = '<'
                        x -= 1
                    else:
                        y += 1
                elif data[y][x - 1] == '#':
                    direct = '^'
                    y -= 1
                else:
                    x -= 1
            except IndexError:
                break
            past_pos.append(pos)
            pos = ((x, y), direct)
            if pos in past_pos:
                print('loops\n')
                past_pos = []
                total += 1
                break
        data = orig_data.copy()
print(total)