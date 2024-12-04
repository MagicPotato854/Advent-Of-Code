# Read in the data
with open('DAY1\day1.txt', 'r') as data:
    data = [i.rstrip('\n') for i in data.readlines()]

# Split the data into two lists of numbers
list1, list2 = [i.split('   ')[0] for i in data], [i.split('   ')[1] for i in data]
total = 0

# Count the # of occurences of a # in list 2 and multiply them by the orig number
for num in list1:
    total += list2.count(num) * int(num)
print(total)