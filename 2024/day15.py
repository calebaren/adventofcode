#day15 pt1
with open("day15_moves.txt") as file:
	# read in the moves
	moves = ''.join(line.rstrip() for line in file.read())

with open("day15_map.txt") as file:
	# read in the map
	grid = [list(line.rstrip()) for line in file]
# simulate
# keep track of where the boxes are.
# if we move and we step on a box, we try to push that box in the same direction.
# if there's a box on the other side, we keep trying to push boxes until we either hit an empty space (in which case, we succeed)
# or we hit a wall, in which case we ignore the direction.
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

def simulate(moves, grid):
	# store the robot's position
	x,y = get_robot(grid)
	for m in moves:
		# print(f"~~~~~~~~~~~~~~~~~~~~~~~")
		# print(f"MOVE: {m}: {x}{y}")
		dx, dy = DIRECTIONS[m]
		if grid[x+dx][y+dy] == ".":
			# move to that square.
			# print("empty square")
			grid[x][y] = "."
			x += dx 
			y += dy
			grid[x][y] = "@"
		elif grid[x+dx][y+dy] == "#":
			# print("hit wall")
			continue
		else:
			# this is a box.
			row_boxes = []
			i = 1
			while True:
				# if there are more boxes in the stack, we should append them to the row_box.
				if grid[x+(i*dx)][y+(i*dy)] == "O":
					row_boxes.append((x+(i*dx),y+(i*dy)))
					i += 1
				elif grid[x+(i*dx)][y+(i*dy)] == "#":
					# we've hit a wall. don't move the robot. ignore the boxes.
					break
				else: 
					# we've hit an empty square. we should leapfrog the first box to the empty square.
					grid[x+(i*dx)][y+(i*dy)] = "O"
					grid[x+dx][y+dy] = "."

					grid[x][y] = "."
					x += dx 
					y += dy
					grid[x][y] = "@"
					break
	return grid

# driver
def get_GPS(moves, grid):
	# print(*grid, sep="\n")
	final_grid = simulate(moves, grid)
	# print(*final_grid, sep="\n")
	m, n = len(grid), len(grid[0])
	res = 0
	for i in range(m):
		for j in range(n):
			if final_grid[i][j] == "O":
				res += 100*i +j
	return res

print(f'Final sum of GPS coordinates: {get_GPS(moves, grid)}')
