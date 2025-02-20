# day6 pt1

with open("day6.txt") as file:
	maparea = [list(line.rstrip()) for line in file]

m, n = len(maparea), len(maparea[0])
DIRECTIONS = [(-1,0),(0,1),(1,0),(0,-1)]

def find_starting_point(maparea):
	for i in range(m):
		for j in range(n):
			if maparea[i][j] == "^":
				return (i,j)
starting_x, starting_y = find_starting_point(maparea)

def count_steps(i,j):
	# i, j are the starting positions.
	# we step forward until we either hit an obstacle, or leave the map area.
	d = 0
	seen = set([(i,j)])
	di, dj = DIRECTIONS[d]

	while True:
		if not (0 <= i+di < m and 0 <= j+dj < n):
			break
		# otherwise, if we see an obstacle, we swivel and don't step forward.
		if maparea[i+di][j+dj] == '#':
			d = (d+1)%4
			di, dj = DIRECTIONS[d]
		else:
			i += di
			j += dj
			seen.add((i,j))
	return len(seen)

# driver
number_steps = count_steps(starting_x, starting_y)
print(f'Number of steps the guard took: {number_steps}')

# day5 pt 2
def stuck_in_loop(i, j):
	# i, j are the starting positions.
	# we step forward until we either hit an obstacle, or leave the map area.
	d = 0
	seen = set([(i,j, d)])
	di, dj = DIRECTIONS[d]

	while True:
		if not (0 <= i+di < m and 0 <= j+dj < n):
			break
		
		if maparea[i+di][j+dj] == '#':
			d = (d+1)%4
			di, dj = DIRECTIONS[d]
		else:
			i += di
			j += dj
			if (i,j,d) in seen:
				return True
			seen.add((i,j,d))
	
	return False

# driver
number_of_loops = 0
for r in range(m):
	for c in range(n):
		if maparea[r][c] != ".": continue
		maparea[r][c] = "#"
		if stuck_in_loop(starting_x, starting_y): number_of_loops += 1
		maparea[r][c] = "."
print(f'Number of loops: {number_of_loops}')
