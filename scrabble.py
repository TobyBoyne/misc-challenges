"""For the tile frequency and values given in scrabble-values.txt, how many unique ways can you chose a
7-letter hand worth exactly 46 points?"""

import numpy as np
from parse import parse

def get_values():
	with open('txt-files/scrabble-values.txt') as f:
		tile_values = np.zeros((27, 2))
		for i, line in enumerate(f):
			_, *count_value = parse('{},{:d},{:d}', line.strip('\n'))
			tile_values[i, :] = count_value
	return tile_values


def find_all_combinations(points, used, target):
	# points must be sorted
	if len(used) == 7:
		return []

	combinations = []
	for i, p in enumerate(points):
		if p == target and len(used) == 6:
			combinations.append(used + [p])
		if p <= target:
			remaining = points[:i]
			combinations += find_all_combinations(remaining, used + [p], target - p)

	return combinations



def num_combinations(tile_values):
	points = list(sorted(tile_values[:, 1]))
	print(points)
	print(find_all_combinations(points, [], 46))

tile_values = get_values()
num_combinations(tile_values)
