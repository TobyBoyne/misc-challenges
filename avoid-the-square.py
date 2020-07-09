from tqdm import tqdm
import numpy as np
from itertools import product

"""
0 -> not assigned
1 -> player 1
2 -> player 2
"""

W = 5
# N is the number of tiles to be placed by player 1
N = np.ceil(W ** 2 / 2)
print(N)

def find_blocked_tiles(b):
	"""Finds all tiles that are not valid as would form a square"""
	return b

def get_all_squares():
	"""Returns a dictionary of form
	(x, y): list of square masks that include tile at (x, y)"""
	mask_dict = {(x, y): [] for (x, y) in product(range(W), repeat=2)}
	ROT = np.array([[0, 1], [-1, 0]])
	square_vectors = [np.array([y, 1]) for y in range(0, W)]
	square_vectors += [np.array([1, x]) for x in range(2, W)]

	print(np.dot(ROT, np.array([1, 2])))

	for vector in square_vectors:
		for r in range(1, W):
			move_vec = r * vector
			dy, dx = move_vec
			# only go through (x, y) where the square's bounding box is within the board
			for y, x in product(range(0, W-dy-dx), range(dy, W-dx)):
				cur_pos = np.array([y, x], dtype=np.int)
				mask = np.zeros((W, W))
				for t in range(4):
					# try:
					# 	mask[tuple(cur_pos)] = 1
					# except IndexError:
					# 	print(f"{mask}\n{x=},{y=}\n{move_vec=}\n{cur_pos=}")
					# 	raise ValueError
					mask[tuple(cur_pos)] = 1

					cur_pos += move_vec
					move_vec = np.dot(ROT, move_vec)

				print(mask)



	# squares = [unit_square * r for r in range(1, W+1)]
	# print(squares)
	return mask_dict


get_all_squares()



empty_board = np.zeros((W, W), dtype=np.int)

prev_boards = [empty_board]
# filled_boards contained all boards where player 1 has not made a square
filled_boards = []

# while prev_boards:
# 	cur_boards = prev_boards
# 	prev_boards = []
# 	for board in cur_boards:
# 		if board.sum() == N:
# 			filled_boards.append(board)
# 		else:
# 			for (x, y) in product(range(3), 2):
# 				if board[y, x] == 0:
# 					board[y, x] = 1
# 					new_board = find_blocked_tiles(board)
# 					prev_boards.append(new_board)
#
#

