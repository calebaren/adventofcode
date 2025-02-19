# day7 pt1
from collections import deque

with open("day7.txt") as file:
	data = [line.rstrip() for line in file.read().splitlines(True)]

def possibly_true(s):
	# for a given string, split into the final result and the operands
	test_value, operands = s.split(": ")
	test_value = int(test_value)
	operands = list(map(int, operands.split(" ")))

	# for each pair of operands, we evaluate left to right. iterate over each temporary result.
	q = [operands[0]]
	for op in operands[1:]:
		new_q = []
		for temp in q:
			# try multiplying. if we don't bust, then do the operation.
			if temp * op <= test_value: new_q.append(temp*op)

			# try adding. if we don't bust, then do the operation.
			if temp + op <= test_value: new_q.append(temp+op)
		q = new_q
	return test_value if test_value in q else 0

# driver
calibration_result = sum(possibly_true(line) for line in data)
print(f'Calibration result: {calibration_result}')

# day7 pt2
def possibly_true_with_concatenation(s):
	# for a given string, split into the final result and the operands
	test_value, operands = s.split(": ")
	test_value = int(test_value)
	operands = list(map(int, operands.split(" ")))

	q = [operands[0]]
	for op in operands[1:]:
		new_q = []
		for temp in q:
			# try multiplying. if we don't bust, then do the operation.
			if temp * op <= test_value: new_q.append(temp*op)

			# try adding. if we don't bust, then do the operation.
			if temp + op <= test_value: new_q.append(temp+op)

			# try concatenating.
			if int(str(temp) + str(op)) <= test_value: new_q.append(int(str(temp) + str(op)))
		q = new_q

	return test_value if test_value in q else 0

calibration_result_with_concatenation = sum(possibly_true_with_concatenation(line) for line in data)
print(f'Calibration result with concatenation: {calibration_result_with_concatenation}')