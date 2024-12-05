# Read in the data
with open('2024/DAY5/day5.txt', 'r') as data:  # With test5.txt should return 143
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
    
    # Check each update (line) to see if it's valid
    else:
        valid = True
        updates = line.split(',')
        for index, page in enumerate(updates):
            if not valid:
                break
            try:
                for page_rule in rules[page]:
                    try:
                        if updates.index(page_rule) < index:
                            valid = False
                            break
                    except ValueError:
                        continue
            except KeyError:
                continue

        # Add the middle page of valid updates to the total
        if valid:
            total += int(updates[len(updates) // 2])
print(total)