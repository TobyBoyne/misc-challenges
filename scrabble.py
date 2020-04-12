"""For the tile frequency and values given in scrabble-values.txt, how many unique ways can you chose a
7-letter hand worth exactly 46 points?

Key insights:
 - Must begin with 10, 10, 8, 8 to reach 46 points
 - Remaining combinations to get to exactly 46 are shown in COMBS
 - There are enough copies of each letter below 8-points to not worry about the count of each tile"""

import numpy as np
from parse import parse
from itertools import combinations_with_replacement

def get_values():
	with open('txt-files/scrabble-values.txt') as f:
		tile_values = np.zeros((27, 2), dtype=int)
		grouped_letters = {}
		for i, line in enumerate(f):
			letter, count, value = parse('{},{:d},{:d}', line.strip('\n'))
			tile_values[i, :] = [count, value]
			grouped_letters[value] = grouped_letters.get(value, []) + [letter]
	print(grouped_letters)
	return tile_values, grouped_letters


def combs_to_target(points, r, target):
	return (comb for comb in combinations_with_replacement(points, r) if sum(comb) == target)

def find_all_combinations(points):
	COMBS = combs_to_target((1, 2, 3, 4, 5), 3, 10)

	combinations = []
	for comb in COMBS:
		sub_combinations = ['']
		for p in set(comb):
			new_subs = []
			for i, sub in enumerate(sub_combinations):
				for new_letters in combinations_with_replacement(points[p], comb.count(p)):
					new_subs.append(sub + ''.join(new_letters))
			sub_combinations = new_subs
		combinations += sub_combinations

	return combinations



def brute_force(tile_values, grouped_letters):
	all_combs = find_all_combinations(grouped_letters)
	print(all_combs)
	return len(all_combs)

tile_values, grouped_letters = get_values()
print(brute_force(tile_values, grouped_letters))
