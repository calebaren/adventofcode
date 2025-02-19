# day6 pt1

with open("day6.txt") as file:
	maparea = [line.rstrip() for line in file]

# the guard starts with "^".
# we rotate through 4 directions, turning right by 90 degrees each time.
def count_steps(i,j):
	m, n = len(maparea), len(maparea[0])
	DIRECTIONS = [(-1,0),(0,1),(1,0),(0,-1)]

	# i, j are the starting positions.
	# we step forward until we either hit an obstacle, or leave the map area.
	d = 0
	seen = set([(i,j)])
	# algorithm: look at my current square.
	# if it's off the map, break the loop.
	# if the next is an obstacle, then swivel and step.
	# otherwise, just step forward.
	# if this step is valid, then take a step forward. otherwise, break the while loop.
	# next_i = i + DIRECTIONS[d][0]
	# next_j = j + DIRECTIONS[d][1]
	while 0 <= i < m and 0 <= j < n:
		next_i =  i + DIRECTIONS[d][0]
		next_j = j + DIRECTIONS[d][1]

		# if we've stepped off the map, break and return the length of the set.
		if not (0 <= next_i < m and 0 <= next_j < n):
			break

		# otherwise, if we see an obstacle, we swivel and don't step forward.
		if maparea[next_i][next_j] == "#":
			d = (d+1) % 4

		# otherwise, we step forward.
		else:
			i,j = next_i,next_j
			seen.add((i,j))
	return len(seen)

def find_starting_point(maparea):
	for i, row in enumerate(maparea):
		for j, x in enumerate(row):
			if x == "^":
				return (i,j)

# driver
number_steps = count_steps(*find_starting_point(maparea))
print(f'Number of steps the guard took: {number_steps}')

# day5 pt 2
# 
