# day23 pt1
import math
import collections

with open("day23.txt") as file:
	data = [line.rstrip().split("-") for line in file]

# each is a bidirectional connection
# we can track down the set of 3 by looping through them in a sorted way?
# alternatively, we can generate all 3-groups, then divide by the number of overcounts (which is 3! or 6.)
# how many 3-groups can we generate?
# start with each person as the vertex of the triangle. then, if they're connected to x other people, there are x(x-1) ways to connect to them.
graph = collections.defaultdict(list)
for u, v in data:
	# only add 1 way: from the alphabetically smaller one to the bigger one. that way, we don't overcount.
	if u > v:
		graph[v].append(u)
	else:
		graph[u].append(v)

# start iterating through an outer loop.
res = 0
for k in sorted(graph.keys()):
	# if the key contains a t, then all linked are valid. 
	if 't' in k:
		res += math.comb(len(graph[k]), 2)
	else:
	# if the key doesn't contain a t, then we exclude all the combinations with 0 ts.
		no_ts = [computer for computer in graph[k] if 't' not in computer]
		res += math.comb(len(graph[k]), 2) - math.comb(len(no_ts), 2)
print(f'combos: {res}')

# have to be more stringent: classes of 