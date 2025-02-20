# day10 pt1

with open("day10.txt") as file:
	data = [[int(i) for i in line.rstrip()] for line in file]


def trailhead_score(data):
	m, n = len(data), len(data[0])

	def dfs(i,j):
		nonlocal seen
		# we don't consider separate paths. 
		# so for this trailhead, we need to keep track of which ones we've seen.
		if data[i][j] == 9:
			seen.add((i,j))
			return

		for di, dj in [(0,1),(1,0),(0,-1),(-1,0)]:
			ni, nj = i+di, j+dj
			if 0 <= ni < m and 0 <= nj < n and data[ni][nj] == data[i][j] + 1:
				dfs(ni,nj)

	total_score = 0
	for i in range(m):
		for j in range(n):
			if data[i][j] == 0:
				seen = set()
				dfs(i,j)
				total_score += len(seen)
	return total_score

print(f'Trailhead scores: {trailhead_score(data)}')


# day10 pt2
def trailhead_rating(data):
	m, n = len(data), len(data[0])

	def dfs(i,j):
		nonlocal rating
		if data[i][j] == 9:
			rating += 1
			return

		for di, dj in [(0,1),(1,0),(0,-1),(-1,0)]:
			ni, nj = i+di, j+dj
			if 0 <= ni < m and 0 <= nj < n and data[ni][nj] == data[i][j] + 1:
				dfs(ni,nj)

	total_rating = 0
	for i in range(m):
		for j in range(n):
			if data[i][j] == 0:
				rating = 0
				dfs(i,j)
				total_rating += rating
	return total_rating

print(f'Trailhead ratings: {trailhead_rating(data)}')

