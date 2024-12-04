# Read in the data
with open('day4.txt', 'r') as data:  # Should be 9 for test4part2.txt
    data = [i.rstrip('\n') for i in data.readlines()]
    data_ls = [list(i) for i in data]

# Look for A's and check corners to see if they make a X-MAS
x_mas = 0
for y, line in enumerate(data_ls):  # Y COMES FIRST!!!!!

    # Check if we're on the edge of the board
    if y == 0 or y == len(data_ls) - 1:
        continue

    for x, char in enumerate(line):

        # Check if we're on the edge of the board
        if x == 0 or x == len(data_ls[0]) - 1:
            continue

        if char == 'A':
            corners = ''.join([
                data_ls[y - 1][x - 1],  # Top left
                data_ls[y - 1][x + 1],  # Top right
                data_ls[y + 1][x + 1],  # Bottom right
                data_ls[y + 1][x - 1]   # Bottom left
            ])
            if ('MM' in corners or 'SS' in corners) and \
            (corners.count('M') == 2 and corners.count('S') == 2):
                print(corners)
                x_mas += 1
print(x_mas)