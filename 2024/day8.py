# day8 pt1
from collections import defaultdict
from itertools import combinations


with open("day8.txt") as file:
	data = [list(line.rstrip()) for line in file]

# calculate the number of antinodes on the map.
# for a given pair, we have a directed distance from a->b.
# to get the antinodes, we add the directed distance to b, then subtract the distance from a.
def get_num_unique_antinodes(grid):
	# for a given grid, get the number of unique antinodes.

	# store the list of unique positions in a set and return the length of the set
	antinodes_set = set()

	antenna_classes = defaultdict(list)
	# first, build a set of positions.
	m, n = len(grid), len(grid[0])
	for i in range(m):
		for j in range(n):
			if grid[i][j] != "." and grid[i][j] != "#":
				antenna_classes[grid[i][j]].append((i,j))

	# for each antenna class, we should get the antinodes for that class of antennas.
	def generate_antinodes(symbol):
		# there are l choose 2 combinations. we should get all of them, then generate antinodes.
		antinodes = set()
		nodes = antenna_classes[symbol]
		for (a,b), (x,y) in combinations(nodes, 2):
			# directed distance
			dx, dy = x-a, y-b
			if 0 <= x+dx < m and 0 <= y+dy < n:
				antinodes.add((x+dx, y+dy))
			if 0 <= a-dx < m and 0 <= b-dy < n:
				antinodes.add((a-dx, b-dy))
		return set(antinodes)

	# iterate over antenna classes.
	for symbol in antenna_classes:
		antinodes_set |= generate_antinodes(symbol)
	return len(antinodes_set)

print(f'Number of unique antinodes: {get_num_unique_antinodes(data)}')

# day8 pt 2
# we do the same thing, but we just keep going in the same direction.
def get_num_unique_harmonics(grid):
	# for a given grid, get the number of unique antinodes.

	# store the list of unique positions in a set and return the length of the set
	antinodes_set = set()

	antenna_classes = defaultdict(list)
	# first, build a set of positions.
	m, n = len(grid), len(grid[0])
	for i in range(m):
		for j in range(n):
			if grid[i][j] != "." and grid[i][j] != "#":
				antenna_classes[grid[i][j]].append((i,j))

	# for each antenna class, we should get the antinodes for that class of antennas.
	def generate_antinodes(symbol):
		# there are l choose 2 combinations. we should get all of them, then generate antinodes.
		antinodes = set()
		nodes = antenna_classes[symbol]
		for (a,b), (x,y) in combinations(nodes, 2):
			# directed distance
			dx, dy = x-a, y-b

			# keep moving in positive direction
			r = 0
			while 0 <= x+(r*dx) < m and 0 <= y+(r*dy) < n:
				antinodes.add((x+(r*dx), y+(r*dy)))
				r += 1

			# keep moving in negative direction
			r = 0
			while 0 <= a-(r*dx) < m and 0 <= b-(r*dy) < n:
				antinodes.add((a-(r*dx), b-(r*dy)))
				r += 1
		return antinodes

	# iterate over antenna classes.
	for symbol in antenna_classes:
		antinodes_set |= set(generate_antinodes(symbol))
	return len(antinodes_set)

print(f'Number of unique harmonics: {get_num_unique_harmonics(data)}')