import collections
import re

# day14 pt1
with open('day14.txt') as file:
	data = [line.rstrip() for line in file]

# process data
def get_robot(line):
	# gets the position and velocity from a string.
	return list(map(int, re.findall(r"-?\d+", line)))

WIDTH = 101 # width of the room
HEIGHT = 103 # height of the room

def simulate(robot, steps):
	# takes in a position, velocity vector.
	x,y = robot[:2] # (horizontal distance, vertical distance)
	vx,vy = robot[2:] # (horizontal speed, vertical speed)
	return ((x + (vx * steps)) % WIDTH, (y + (vy * steps)) % HEIGHT)

def safety_factor(data):
	# gets the safety factor of all the robots
	def get_quadrant(robot):
		# given a position of robot returns the qudrant
		x, y = robot
		if x == WIDTH//2 or y == HEIGHT//2:
			return None
		return (int(x  < WIDTH//2), int(y < HEIGHT//2))

	d = collections.defaultdict(int)
	for robot in [simulate(get_robot(line), 100) for line in data]:
		if (quad:=get_quadrant(robot)) is not None:
			d[quad] += 1
	res = 1
	for v in d.values():
		res *= v
	return res


print(safety_factor(data))

# day14 pt2

def simulate_steps(robots):
	while True:
		for j in range(len(robots)):
			x,y = robots[j][:2] # (horizontal distance, vertical distance)
			vx,vy = robots[j][2:] # (horizontal speed, vertical speed)
			robots[j][0] = (x + (vx)) % WIDTH
			robots[j][1] = (y + (vy)) % HEIGHT
		yield [r[:2] for r in robots]


def render():
	# takes in an array of robots and renders them
	robot_generator = simulate_steps([get_robot(line) for line in data])
	i = 1
	while True:
		# input()
		# print(f"~~~~~~~~~~~~~~~{i} ------")
		robot_positions = next(robot_generator)
		grid = [[' ' for _ in range(HEIGHT)] for _ in range(WIDTH)]
		for c,r in robot_positions:
			grid[c][r] = '#'
		txt = '\n'.join(''.join(row) for row in grid)
		if '######' in txt:
			print(i)
			input()
			print(txt)
		# print()
		i += 1
render()


