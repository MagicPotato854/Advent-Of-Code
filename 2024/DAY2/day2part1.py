# Read in the data
with open('DAY2\day2.txt', 'r') as data:
    data = [i.rstrip('\n') for i in data.readlines()]

# Determine whether a report is safe or not and add to total # of safe reports
safe_reports = 0
for report in data:
    report = [int(i) for i in report.split(' ')]
    prev_num = None
    diff = []
    # Add the differences between the numbers in a report to a list
    for index, num in enumerate(report):
        if index == 0:
            prev_num = num
            continue
        diff.append(num - prev_num)
        prev_num = num

    # Check for invalid reports by sorting differences and checking ends
    diff.sort()
    if diff[0] < -3 or 0 in diff or diff[-1] > 3 or (diff[0] < 0 and diff[-1] > 0):
        continue
    safe_reports += 1
print(safe_reports)