# day5 pt1
import collections

with open("day5.txt") as file:
	arr = [line.rstrip() for line in file]
	# find index of empty string
	idx_split = [len(a) for a in arr].index(0)

	rules = [tuple(int(i) for i in s.split("|")) for s in arr[:idx_split]]
	updates = [[int(i) for i in s.split(",")] for s in arr[idx_split+1:]]


# build dependency graph:
graph = collections.defaultdict(set) # int
for u, v in rules:
	graph[u].add(v)

def is_valid_update(update):
	# step through.
	# graph[u] contains the pages that MUST follow u. 
	# so if we check graph[update[i]] and we've already seen this, then this is false.
	seen = set()
	for u in update:
		seen.add(u)
		# if we've seen any nodes alreayd that are supposed to come after, then we break as false.
		if graph[u] & seen:
			return False
	return True

def get_middle_element(update):
	return update[len(update)//2]


# driver
sum_of_valid_updates = sum(get_middle_element(update) for update in updates if is_valid_update(update))
print(f'Sum of middle page numbers of valid updates: {sum_of_valid_updates}')

# day5 pt2
# topologically sort the pages.
def topological_sort(update):
	all_nodes = set(update)
	new_graph = {u: v & all_nodes for u, v in graph.items() if u in all_nodes}

	# build topological sort
	indegree = collections.defaultdict(int)
	for u in new_graph:
		for v in new_graph[u]:
			indegree[v] += 1
	
	# start a list of nodes with 0 indegrees.
	queue = collections.deque([k for k in update if indegree[k] == 0])
	res = []
	while queue:
		node = queue.popleft()
		res.append(node)
		for v in graph[node]:
			indegree[v] -= 1 # remove this edge
			if indegree[v] == 0:
				# add this to be processed next
				queue.append(v)
	return res

sum_of_sorted_updates = sum(get_middle_element(topological_sort(update)) for update in updates if not is_valid_update(update))
print(f'Sum of middle page numbers of SORTED updates: {sum_of_sorted_updates}')
