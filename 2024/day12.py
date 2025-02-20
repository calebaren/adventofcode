# day12 pt1
from collections import deque

with open("day12.txt") as file:
	data = [list(line.rstrip()) for line in file]
	# data = list(map(list, file.read().splitlines(True)))


def get_area(grid):
	m,n = len(grid), len(grid[0])
	# for each region, conduct bfs.
	def bfs(i,j, grid):
		q = deque([(i,j)])
		area = 0
		total_perimeter = 0
		while q:
			i, j = q.popleft()
			for di,dj in [(0,1),(1,0),(-1,0),(0,-1)]:
				ni, nj = i+di, j+dj
				if 0<=ni<m and 0<=nj<n and grid[ni][nj] == grid[i][j] and grid[ni][nj] != " ":
						q.append((ni,nj))
						area += 1
				else:
					total_perimeter += 1

			# the contribution to the perimer = 4 - number of neighbors.
			# total_perimeter += (4 - neighbors)
			grid[i][j] = " " # mark as seen.

			
		return (area, total_perimeter)

	for i in range(m):
		for j in range(n):
			if data[i][j] != " ":
				print(data[i][j], bfs(i,j, data))
				# print(*data, sep = "\n")

print(get_area(data))