# day 2: pt 1

with open("day2.txt") as file:
	reports = [[int(i) for i in line.split()] for line in file]

def check_safe(report):
	diffs = [b-a for a, b in zip(report, report[1:])]
	# first condition: either all increasing or all decreasing.
	# second condition: differences must be at least 1 and at most 3.
	return 1 <= min(diffs) <= max(diffs) <= 3 or -3 <= min(diffs) <= max(diffs) <= -1

safe_reports = sum(check_safe(report) for report in reports)
print(f"Safe reports: {safe_reports}")

# day2: pt 2
# we can just remove one from each report.
def check_safe_dampened(report):
	return any(check_safe(report[:i] + report[(i+1):]) for i in range(len(report)))

safe_reports_dampener = sum(check_safe_dampened(report) for report in reports)
print(f"Safe reports with dampener: {safe_reports_dampener}")
