def safe_checker(report):
    """
    Checks whether a list of numbers meets the following requirements:
    1. The distance between each consecutive # must be less than 3 and not 0
    2. All numbers must be ascending or descending
    If requirements are met, return True, if not, return False.
    """
    prev_num = None
    diff = []
    for index, num in enumerate(report):
        if index == 0:
            prev_num = num
            continue
        diff.append(num - prev_num)
        prev_num = num
    diff.sort()
    if diff[0] < -3 or 0 in diff or diff[-1] > 3 or (diff[0] < 0 and diff[-1] > 0):
        return False
    return True

# Read in the data
with open('DAY2\day2.txt', 'r') as data:
    data = [i.rstrip('\n') for i in data.readlines()]

# Check if a report is safe, if not, see if removing one number makes it safe
safe_reports = 0  # Total up # of safe reports
for report in data:
    report = [int(i) for i in report.split(' ')]
    if safe_checker(report):
        safe_reports += 1
    else:
        for index, _ in enumerate(report):
            test_report = report.copy()
            test_report.pop(index)
            if safe_checker(test_report):
                safe_reports += 1
                break
print(safe_reports)