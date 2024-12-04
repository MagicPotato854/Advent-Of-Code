# Read in the data
with open('day1.txt', 'r') as data:
    data = [i.rstrip('\n') for i in data.readlines()]

# Split the data into two lists of numbers
list1, list2 = [i.split('   ')[0] for i in data], [i.split('   ')[1] for i in data]
list1.sort()
list2.sort()
total = 0

# Find the distances between sorted items and add them to total
for index, num in enumerate(list1):
    total += abs(int(num) - int(list2[index]))
print(total)