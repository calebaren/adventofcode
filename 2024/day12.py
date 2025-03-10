# day12 pt1
from collections import deque

with open("day12.txt") as file:
	data = [list(line.rstrip()) for line in file]
	# data = list(map(list, file.read().splitlines(True)))

# dfs
# get the perimeter by running dfs on grid i,j
# mark the current grid as seen
# get the neighbors. if the next is not a valid next step, we add to perimeter
# otherwise, we run dfs on the next.

def dfs(i, j, grid, seen):
	m, n = len(grid), len(grid[0])
	perimeter = 0
	area = 0
	stack = [(i, j)]
	type = "O"
	while stack:
		x, y = stack.pop()
		if (x, y) in seen:
			continue
		seen.add((x,y))

		# we count when we pop from the stack.
		area += 1

		for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
			nx, ny = x+dx, y+dy
			# we count perimeter when the bordering is out of bounds or a different type.
			if not(0 <= nx < m and 0 <= ny < n) or grid[nx][ny] != grid[i][j]:
				perimeter += 1
			if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == grid[i][j] and (nx,ny) not in seen:
				stack.append((nx,ny))

	for i, j in seen:
		grid[i][j] = "."
	return (area, perimeter)


# dfs(0, 0, data, set())

def get_perimeter_and_area(grid):
	m, n = len(grid), len(grid[0])

	price = 0
	for i in range(m):
		for j in range(n):
			if grid[i][j] != ".":
				area, perimeter = dfs(i, j, grid, set())
				price += area * perimeter
	return price

print(f"Price of map: {get_perimeter_and_area(data)}")

# day12 pt2
# get edges
# 
