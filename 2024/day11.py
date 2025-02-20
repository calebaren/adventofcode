# day11 pt1
from functools import cache
from collections import deque, defaultdict

with open("day11.txt") as file:
	stones = list(map(int, file.read().rstrip().split(" "))) # keep as a string to prevent overflow


def process_stones(stones, blinks):
	def change_stone(stone):
		if int(stone) == 0:
			return [1]
		str_stone = str(stone)
		n = len(str_stone)
		if n % 2 == 0:
			return [int(str_stone[:n//2]), int(str_stone[n//2:])]
		else:
			return [2024 * stone]

	queue = deque(stones)
	for _ in range(blinks):
		new_queue = deque()
		while queue:
			stone = queue.popleft()
			new_queue.extend(change_stone(stone))
		queue = new_queue
	return len(queue)

print(f'Number of stones after blinking 25 times: {process_stones(stones, 25)}')


# day11 pt2
def recursive_process_stones(stones, blinks):
	@cache
	def recursive_change_stone(stone, blinks):
		# basecase
		if blinks == 0:
			return 1 

		res = 0
		# first case: change to 1
		if stone == 0:
			res = recursive_change_stone(1, blinks-1)

		# second case: split number in half
		elif len(str_stone := str(stone)) % 2 == 0:
			n = len(str_stone)
			res = recursive_change_stone(int(str_stone[:n//2]), blinks-1)
			res += recursive_change_stone(int(str_stone[n//2:]), blinks-1)

		# third case: multiply by 2024
		else:
			res = recursive_change_stone(stone * 2024, blinks-1)
		return res

	return sum(recursive_change_stone(s, blinks) for s in stones)
	# return res

print(f'Number of stones after blinking 75 times (recursive): {recursive_process_stones(stones, 75)}')