# day16 pt1

with open("day16.txt") as file:
	grid = [list(line.rstrip()) for line in file]


# backtracking: pathfinding algorithm
# we have to keep track of hte current position and direction
# get a list of next paths
# if they are on the same path, don't incur a score, add 1
# if they are in a different direction, update direction and add 1 + 1000. we would never go backwards.

def searching_for_end(grid):
	m, n = len(grid), len(grid[0])
	# to avoid maximum recursion depth, we'll refactor to use a stack.
	stack = []
	# stack contains the position and the direction.
	for i in range(m):
		for j in range(n):
			if grid[i][j] == 'S':
				stack.append((i, j, 0, 1, 0))

	best = float('inf')
	grid[i][j] = '#'
	while stack:
		i, j, di, dj, score = stack.pop()
		print(i, j, di, dj, score)
		if grid[i][j] == 'E':
			print(*grid, sep="\n")
			best = min(best, score)
			print(best)
			continue

		
		# move forward:
		if 0 <= (ni:=i+di) < m and 0 <= (nj:=j+dj) < m and grid[ni][nj] != '#':
			stack.append((ni, nj, di, dj, score+1))

		# move other directions:
		if 0 <= (ni:=i+dj) < m and 0 <= (nj:=j+di) < m and grid[ni][nj] != '#':
			stack.append((ni, nj, dj, di, score+1+1000))

		if 0 <= (ni:=i-dj) < m and 0 <= (nj:=j-di) < m and grid[ni][nj] != '#':
			stack.append((ni, nj, -dj, -di, score+1+1000))
		grid[i][j] = '.'

	
	return best

print(f'Best score: {searching_for_end(grid)}')