# import heapq
import collections

# day 1: part 1
lefts = []
rights = []

# sort left and right
with open("day1.txt") as file:
	for line in file:
		# print(re.split(r'\s+', line.rstrip()))
		processed_str = line.rstrip().split(" ")
		lefts.append(int(processed_str[0]))
		rights.append(int(processed_str[-1]))


lefts.sort()
rights.sort()
n = len(lefts)
total_distance = sum(abs(a-b) for a,b in zip(lefts, rights))
print(f'Total distance: {total_distance}')

# day 1: part 2
# for each number in the left list, multiply by the number of times it appears in the right.
d_right = collections.Counter(rights)
total_similarity = sum(d_right[l] * l for l in lefts)
print(f'Total similarity: {total_similarity}')