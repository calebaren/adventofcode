# day9 pt1
from collections import deque

with open("day9.txt") as file:
	data = file.read().rstrip()

# comment this out when done testing.
# data = "2333133121414131402"

def compact_file(data):
	# simulate with a stack.
	data = list(map(int, data))
	stack = []
	for i, x in enumerate(data):
		if i % 2 == 0:
			stack += [i // 2] * x
		else:
			# this is free space.
			stack += [None] * x

	i = 0 # pointer to the leftmost free space.
	while i < len(stack):
		# first, always remove the empty blocks at the end.
		while stack[-1] is None:
			stack.pop()

		# move the pointer to the leftmost freespace.
		while i < len(stack) and stack[i] is not None:
			i += 1

		# if we've freed up all our space, then there are no more and we exit.
		if i >= len(stack):
			break

		stack[i] = stack.pop()

	return stack

def check_sum(optimized_data):
	checksum = 0
	for position, idx in enumerate(optimized_data):
		if idx is not None:
			checksum += idx * position 
	return checksum

# driver
print(f'Checksum after compacting file: {check_sum(compact_file(data))}')


# day9 pt 2
# now, we can only store continuous blocks of data.
def compact_blocks(data):
	data = list(map(int, data))

	# file_blocks: (size, idx of starting position, idx of file system.
	file_blocks = []

	# free space: (size, idx of starting position)
	free = []

	idx = 0
	for i, size in enumerate(data):
		if i % 2 == 0:
			file_blocks.append([size, idx, i//2])
		else:
			free.append([size, idx])
		idx += size

	
	# we attempt to move the memory just once.
	# for each memory block, we should greedily try to move it to the empty spot in front.
	for j in range(len(file_blocks)-1, -1, -1):
		file_size, file_starting, file_id = file_blocks[j]

		# starting from the first free block:
		i = 0
		while i < len(free):
			free_size, free_starting = free[i]
			if free_starting <= file_starting and free_size >= file_size:
				# we move.
				file_blocks[j] = file_size, free_starting, file_id
				
				free[i] = free_size-file_size, free_starting+file_size
				# move onto the next file block.
				break 
			i += 1

	return file_blocks
		
def check_sum_2(optimized_data):
	check_sum = 0
	for file_size, file_starting, file_id in optimized_data:
		check_sum += sum(i*file_id for i in range(file_starting, file_starting + file_size))
	return check_sum

# driver
print(f'Checksum after compacting file (using continguous blocks): {check_sum_2(compact_blocks(data))}')
