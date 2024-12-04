# Read in the data
with open('day3.txt', 'r') as data:
     data = data.read()

# split the string by the don't()s first, then do()s
sections = [i.split('do()') for i in data.split("don't()")]

# Remove the don't() sections of the input
for index, _ in enumerate(sections):
     if index != 0:
          sections[index].pop(0)

parsed_data = ''.join([''.join(i) for i in sections])  # Turn the data back into a string
args = [i.split(')') for i in parsed_data.split('mul(')]  # split the string to get only sets of arguments
total = 0

# invoke any valid mul() functions and add them together
for arg in args:
     nums = arg[0].split(',')
     numeric = [bool(i.isnumeric()) for i in nums]
     if len(nums) == 2 and False not in numeric:
          total += int(nums[0]) * int(nums[1])
print(total)