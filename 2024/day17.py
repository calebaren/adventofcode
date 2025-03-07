# day17 pt1
import re
from functools import cache

with open("day17.txt") as file:
	register = [0, 0, 0]
	program = []
	for i, line in enumerate(file):
		if 'Register A' in line:
			register[0] = int(re.findall(r'\d+', line)[0])
		elif 'Register B' in line:
			register[1] = int(re.findall(r'\d+', line)[0])
		elif 'Register C' in line:
			register[2] = int(re.findall(r'\d+', line)[0])
		elif 'Program' in line:
			program = [int(x) for x in re.findall(r'\d+', line)]

def literal(operand):
	return operand

# combos: 0-3 = literal, 4=A, 5=B, 6=C, 7 ignore
def combo(operand, register):
	match operand:
		case _ if 0 <= operand <= 3:
			return literal(operand)
		case 4:
			return register[0]
		case 5:
			return register[1]
		case 6:
			return register[2]
		case 7:
			raise Exception("hit 7 in operand.")

# get output as a string.
@cache
def instructions(i, register, program):
	if not (0 <= i <= len(program)-2):
		raise Exception("out of range.")

	nxt, output = None, None

	opcode, operand = program[i], program[i+1]
	match opcode:
		# 0 - adv, performs division of register A by 2^(combo). 
		# output is truncated -> A 
		case 0: 
			register["a"] = register["a"] // 2**combo(operand, register)

		# 1 - bxl, calculates bitwise XOR of B and literal -> B
		case 1:
			register["b"] = register["b"] ^ literal(operand)

		# 2 - bst, gets combo mod 8 -> B 
		case 2:
			register["b"] = combo(operand, register) % 8

		# 3 - jnz, nothing if A == 0, otherwise jumps to literal and we don't increment additionally.
		case 3:
			if register["a"] != 0:
				# jumps.
				nxt = literal(operand)

		# 4 - bxc, calculates B ^ C -> B. we read the operand but do nothing.
		case 4:
			register["b"] = register["b"] ^ register["c"]

		# 5 - out, calculates combo mod 8, then outputs (separated by commas if multiple)
		case 5:
			output = str(combo(operand, register) % 8)

		# 6 - bdv, acts the same as adv but -> B
		case 6:
			register["b"] = register["a"] // 2**combo(operand, register)

		# 7 - cdv, acts the same as adv but -> C
		case 7:
			register["c"] = register["a"] // 2**combo(operand, register)

	nxt = i+2 if nxt is None else nxt
	return (nxt, output)

def run_computer(register, program):
	# goal: loop through the program and determine what it's trying to output.
	# the loop consists of reading in the opcode and getting the operand
	# perform calculations
	# jump to the next location
	i = 0
	output_arr = []
	while True:
		try:
			i, output = instructions(i, register, program)
			if output is not None: output_arr.append(output)
		except Exception:
			return ','.join(output_arr)

# print(f"Output of computer: {run_computer(register.copy(), program.copy())}")

# day17 pt2
def search_for_a(register, program):
	# takes in an initial register and logs a model input.
	model_output = run_computer(register.copy(), program.copy()).split(",")

	# loop through search space of a.
	for a in range(4434000):
		new_register = register.copy()
		new_register['a'] = a
		i = 0
		ptr = 0
		output_arr = []
		while True:
			try:
				i, output = instructions(i, new_register, program)
				if output is not None: 
					output_arr.append(output)
					if model_output[ptr] != output_arr[-1]:
						# print(f"didn't find. {model_output} vs {output_arr}")
						break
					ptr += 1
			except Exception:
				print(','.join(output_arr))
				break

search_for_a(register.copy(), program.copy())