# day13 pt1
from itertools import batched
import re

# each machine contains 1 prize.
# we have to get the claw right over the prize in order to claim it.
# for each machine, decide if the game is winnable.
# if winnable, return the lowest number of tokens necessary.
# if not winnable, return 0.

with open("day13.txt") as file:
	data = [line.rstrip() for line in file if len(line.rstrip()) > 0]


def pull_numbers(s):
	return tuple(int(x) for x in re.findall(r'\d+', s))

def get_tokens(machine_data):
	tokens = 0
	for machine in batched(machine_data, 3):
		# button a
		a_x, a_y = pull_numbers(machine[0])
		b_x, b_y = pull_numbers(machine[1])
		p_x, p_y = pull_numbers(machine[2])

		det = a_x*b_y - a_y*b_x
		if det == 0:
			print("determinant is 0.")
			continue
		u = int((p_x*b_y-p_y*b_x)/det)
		v = int((a_x*p_y-a_y*p_x)/det)
		# check if this matches.

		if u >= 0 and v >= 0 and u*a_x + v*b_x == p_x and u*a_y + v*b_y == p_y:
			tokens += 3*u + v

	return tokens

print(f'Tokens: {get_tokens(data)}')

# day13 pt2
def get_tokens_2(machine_data):
	tokens = 0
	for machine in batched(machine_data, 3):
		# button a
		a_x, a_y = pull_numbers(machine[0])
		b_x, b_y = pull_numbers(machine[1])
		p_x, p_y = (x + 10000000000000 for x in pull_numbers(machine[2]))

		det = a_x*b_y - a_y*b_x
		if det == 0:
			print("determinant is 0.")
			continue
		u = int((p_x*b_y-p_y*b_x)/det)
		v = int((a_x*p_y-a_y*p_x)/det)
		# check if this matches.

		if u >= 0 and v >= 0 and u*a_x + v*b_x == p_x and u*a_y + v*b_y == p_y:
			tokens += 3*u + v

	return tokens
print(f'Tokens (with 10000000000000 added on): {get_tokens_2(data)}')
