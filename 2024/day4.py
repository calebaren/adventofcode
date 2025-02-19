# day4 pt1
with open("day4.txt") as file:
	data = [line.rstrip() for line in file]

# count the number of times XMAS appears forward, backward, vertical, and diagonal.
DIRECTION_VECTORS = {
	"s": (1, 0),
	"n": (-1, 0),
	"e": (0, 1),
	"w": (0, -1),
	"se": (1, 1),
	"sw": (1, -1),
	"ne": (-1, 1),
	"nw": (-1, -1)
}


# for a given direction, search for all the matches of "XMAS".
def find_xmas(d):
	di, dj = DIRECTION_VECTORS[d]
	# calculates the ranges
	i_range = range(0,m) if di == 0 else range(0,m-3) if di == 1 else range(3,m)
	j_range = range(0,n) if dj == 0 else range(0,n-3) if dj == 1 else range(3,n)

	res = 0
	# iterates through the entire grid.
	for i in i_range:
		for j in j_range:
			# gets indices of search string oriented in a certain direction
			idxs = [(i+di*m, j+dj*m) for m in range(4)]

			# generates search string
			search_string = ''.join(data[a][b] for a,b in idxs)
			res += search_string == "XMAS"
	return res

# driver
dirs = ["n","e","s","w","ne","nw","se","sw"]
m, n = len(data), len(data[0])
# iterate through 8 directions
total_xmas = sum(find_xmas(d) for d in dirs)
print(f'Total finds (XMAS): {total_xmas}')


# day4 pt2
# x-mas means that 2 adjacent corners have M and 2 adjacent corners have S.
# for a given center (i,j)
def find_cross_mas(offset):
	# finds the corner indices for this 9x9 square. we rotate through an array of corner indices.
	corner_indices = [(-1,-1),(-1,1),(1,1),(1,-1)]
	corner_indices += corner_indices

	# iterates through the entire grid.
	res = 0
	for i in range(1,m-1):
		for j in range(1,n-1):
			if data[i][j] == "A":
				res += [data[i+di][j+dj] for di, dj in corner_indices[offset:offset+4]] == ["M","M","S","S"]
	return res

# driver
total_cross_mas = sum(find_cross_mas(offset) for offset in range(4))
print(f'Total finds (X-MAS): {total_cross_mas}')