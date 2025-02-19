import re 

# day3 pt1
with open("day3.txt") as file:
	data = file.read().rstrip()

def process_matched_string(s):
	ints = [int(i) for i in s.split(",")]
	return ints[0] * ints[1]

regex_1 = r"(?<=mul\()\d{1,3},\d{1,3}(?=\))"
multiplication_result = sum(process_matched_string(s) for s in re.findall(regex_1,data))
print(f"Sum of multiplication results: {multiplication_result}")

# day 3 pt2

enabled = True
enabled_multiplication_result = 0

# need the indices of the matches. also need the indices of the do() and don't() matches
regex_2 = r"(?<=mul\()[0-9]{1,3},[0-9]{1,3}(?=\))|do\(\)|don't\(\)"
for m in re.finditer(regex_2, data):
	if m.group() == "do()":
		enabled = True
	elif m.group() == "don't()":
		enabled = False
	elif enabled:
		enabled_multiplication_result += process_matched_string(m.group())
print(f"Sum of enabled multiplication results: {enabled_multiplication_result}")