# Read in the data
with open('2024/DAY6/day6.txt', 'r') as data:
    data = [row.rstrip('\n') for row in data]

# Declare and initialize variables
directs = ['^', '>', 'v', '<']
direct = None
guard = True
pos = None
past_pos = []

# Find guard
for y, row in enumerate(data):
    print(str(y).rjust(3), row, sep=' ')
    for x, char in enumerate(row):
        if char in directs:
            pos = ((x, y), char)
            break
print(pos)

# Move the guard until it goes off screen or loops
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
        pass
    past_pos.append(pos)
    pos = ((x, y), direct)
    if pos in past_pos:
        break
coords = set([i[0] for i in past_pos])
print(len(coords))