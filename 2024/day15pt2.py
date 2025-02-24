# day15 pt2
with open("day15_moves.txt") as file:
	# read in the moves
	moves = ''.join(line.rstrip() for line in file.read())

with open("day15_map.txt") as file:
	# read in the map
	grid = [list(line.rstrip()) for line in file]

DIRECTIONS = {
	"^": (-1,0),
	"<": (0,-1),
	"v": (1,0),
	">": (0,1)
}

def get_robot(grid):
	m, n = len(grid), len(grid[0])
	for i in range(m):
		for j in range(n):
			if grid[i][j] == "@":
				return (i,j)

# now the map can move 2 at once.
def simulate_2(moves, grid):
	def double_grid(grid):
		m, n = len(grid), len(grid[0])
		res = []
		for i in range(m):
			row = []
			for j in range(n):
				match grid[i][j]:
					case '#':
						row.append('#')
						row.append('#')
					case '@':
						row.append('@')
						row.append('.')
					case 'O':
						row.append('[')
						row.append(']')
					case '.':
						row.append('.')
						row.append('.')
			res.append(row)
		return res
	
	def process_step(move, g):
		nonlocal x, y
		dx, dy = DIRECTIONS[move]
		nx, ny = x+dx, y+dy
		# hit a wall
		if g[nx][ny] == "#":
			# position keeps the same
			print("hits a wall")
			return g

		# hit an empty square:
		if g[nx][ny] == ".":
			print("empty square")
			g[x][y] = "."
			g[nx][ny] = "@"
			x,y = nx, ny
			return g

		# hit a box.
		boxes = [] # stores the position of boxes.
		stack = [(nx, ny)] # dfs
		while stack:
			candidate_x, candidate_y = stack.pop()
			if g[candidate_x][candidate_y] == "#":
				print("hit wall at end")
				# do nothing
				return g
			# hit the box vertically
			elif g[candidate_x][candidate_y] in "[]" and dx == 0:
				stack.append((candidate_x+dx, candidate_y+dy))
				boxes.append((candidate_x, candidate_y))
			elif g[candidate_x][candidate_y] == "[" and dy == 0:
				stack.append((candidate_x+dx, candidate_y+dy))
				stack.append((candidate_x+dx, candidate_y+dy+1))
				boxes.append((candidate_x, candidate_y))
				boxes.append((candidate_x, candidate_y+1))
			elif g[candidate_x][candidate_y] == "]" and dy == 0:
				stack.append((candidate_x+dx, candidate_y+dy))
				stack.append((candidate_x+dx, candidate_y+dy-1))
				boxes.append((candidate_x, candidate_y))
				boxes.append((candidate_x, candidate_y-1))
		print("valid box moves")
		while boxes:
			cx, cy = boxes.pop()
			g[cx+dx][cy+dy], g[cx][cy]= g[cx][cy],g[cx+dx][cy+dy]

		# while grid[x+(i*dx)][y+(i*dy)] == "[":
		# 	# if there are more boxes in the stack, we should append them to the row_box.
		# 	boxes.append((x+(i*dx),y+(i*dy)))
		# 	i += 1

		# if the last one is a wall, then we do nothing.
		# if grid[x+(i*dx)][y+(i*dy)] == "#":
		# 	return

		# # we've hit an empty square. 
		# # process all the box positions.
		# grid[x+(i*dx)][y+(i*dy)] = "O"
		# grid[x+dx][y+dy] = "."

		# advances robot.
		g[x][y] = "."
		g[nx][ny] = "@"
		x,y = nx, ny
		return g

	
	expanded_grid = double_grid(grid)

	# store the robot's position
	x, y = get_robot(expanded_grid)
	# print(*map(lambda x: ''.join(x), expanded_grid), sep='\n')
	for m in moves:
		# print(f'~~~~~~~~~~~~~~ {m} ~~~~~~~~~~~')
		expanded_grid = process_step(m, expanded_grid)
		# print(*map(lambda x: ''.join(x), expanded_grid), sep='\n')
	# for m in moves:
	# 	process_step(m)
	return expanded_grid

# driver
def get_GPS(moves, grid):
	final_grid = simulate_2(moves, grid)
	print(*map(lambda x: ''.join(x), final_grid), sep='\n')

	m, n = len(grid), len(grid[0])
	res = 0
	for i in range(m):
		for j in range(n):
			if final_grid[i][j] == "O":
				res += 100*i +j
	return res

print(f'Final sum of GPS coordinates after doubling: {get_GPS(moves, grid)}')