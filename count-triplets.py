# https://www.hackerrank.com/challenges/count-triplets-1/problem

import math
import os
import random
import re
import sys
from collections import Counter


# Complete the countTriplets function below.
def countTriplets(arr, r):
	# value : number of times that value has occured so far
	if r == 1:
		# special case for r==1
		# simply n choose 3 for each unique value in the array
		count = Counter(arr)

		S = sum(n * (n - 1) * (n - 2) / 6 for n in count.values())
		return int(S)
	values_count = {}

	# value : number of times the previous term in the sequence has occured
	prev_values = {}
	total_triplets = 0
	for i, value in enumerate(arr):
		if value not in values_count:
			values_count[value] = 0
		values_count[value] += 1

		if value % r == 0:
			prev = value // r
			if prev not in values_count: continue
			if value not in prev_values:
				prev_values[value] = 0
			prev_values[value] += values_count[prev]

			if prev % r == 0:
				twice_prev = prev // r
				if twice_prev not in values_count: continue

				# prev may not be in prev_values if out of order
				if prev in prev_values:
					total_triplets += prev_values[prev]

	print(total_triplets)
	return total_triplets


if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	nr = input().rstrip().split()

	n = int(nr[0])

	r = int(nr[1])

	arr = list(map(int, input().rstrip().split()))

	ans = countTriplets(arr, r)

	fptr.write(str(ans) + '\n')

	fptr.close()
