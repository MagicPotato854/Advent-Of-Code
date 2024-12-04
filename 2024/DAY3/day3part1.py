# Read in the data
with open('day3.txt', 'r') as data:
     data = data.read()

# split the string by mul( funcs
args = [i.split(')') for i in data.split('mul(')]
total = 0

# invoke any valid mul() functions and add them together
for arg in args:  
     nums = arg[0].split(',')
     numeric = [bool(i.isnumeric()) for i in nums]
     if len(nums) == 2 and False not in numeric:
          total += int(nums[0]) * int(nums[1])
print(total)