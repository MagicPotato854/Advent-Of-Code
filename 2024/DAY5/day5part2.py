# Read in the data
with open('2024/DAY5/day5.txt', 'r') as data:  # With test5.txt should return 123
    data = [i.rstrip('\n') for i in data.readlines()]

# Declare and initialize variables
rules = {}
on_rules = True
total = 0

for line in data:
    # Check if we are switching from rules to updates
    if not line:
        on_rules = False
        continue

    # Put all of the rules into a dictionary
    if on_rules:
        line = line.split('|')
        try:
            rules[line[0]].append(line[1])
        except KeyError:
            rules[line[0]] = [line[1]]

    # Check each update (line) to see if it's invalid
    else:
        valid = True
        updates = line.split(',')
        for index, page in enumerate(updates):
            real_index = index
            page_valid = False

            # While loop fixes invalid updates and marks them invalid
            while not page_valid:
                page_valid = True
                try:
                    for page_rule in rules[page]:
                        try:
                            if updates.index(page_rule) < real_index:
                                updates.pop(real_index)
                                updates.insert(real_index - 1, page)
                                real_index -= 1
                                page_valid = False
                                valid = False
                        except ValueError:
                            continue
                except KeyError:
                    continue

        # Add the middle page of invalid updates to the total
        if not valid:
            total += int(updates[len(updates) // 2])
print(total)