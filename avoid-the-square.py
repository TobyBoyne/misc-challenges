from tqdm import tqdm
import numpy as np
from itertools import product, combinations
from math import comb

"""
https://www.think-maths.co.uk/avoidthesquare
"""

W = 5
# N is the number of pieces placed by player 2
N = W ** 2 // 2

class Combiner:
	def __init__(self, *args):
		self._it = combinations(*args)
		self._len = comb(W**2, N)

	def __iter__(self):
		return self._it

	def __len__(self):
		return self._len

def get_all_squares():
	"""Returns a list of all_masks"""
	all_masks = []
	ROT = np.array([[0, 1], [-1, 0]])
	square_vectors = [np.array([y, 1]) for y in range(0, W)]
	square_vectors += [np.array([1, x]) for x in range(2, W)]

	for vector in square_vectors:
		for r in range(1, W):
			move_vec = r * vector
			dy, dx = move_vec
			# only go through (x, y) where the square's bounding box is within the board
			for y, x in product(range(0, W-dy-dx), range(dy, W-dx)):
				cur_pos = np.array([y, x], dtype=np.int)
				mask = np.zeros((W, W), dtype=np.bool)
				for t in range(4):
					# try:
					# 	mask[tuple(cur_pos)] = 1
					# except IndexError:
					# 	print(f"{mask}\n{x=},{y=}\n{move_vec=}\n{cur_pos=}")
					# 	raise ValueError
					pos_tuple = tuple(cur_pos)
					mask[pos_tuple] = True

					cur_pos += move_vec
					move_vec = np.dot(ROT, move_vec)
				all_masks.append(mask)

	return all_masks


def gen_all_boards():
	tqdm_iter = tqdm(Combiner(range(W**2), N))
	boards = []
	for pieces in tqdm_iter:
		board = np.zeros(25, dtype=np.bool)
		for i in pieces:
			board[i] = True

		boards.append(board.reshape((W, W)))
	print(boards[0])
	return boards


def no_squares(board):
	for mask in all_masks:
		prod = np.logical_and(board, mask)
		if np.count_nonzero(prod) == 4:
			return False
	return True



all_masks = get_all_squares()
boards = gen_all_boards()

valid_boards = []
all_boards_iter = tqdm(boards)
valid_count = 0
for i, board in enumerate(all_boards_iter):
	if no_squares(board):
		valid_boards.append(board)
		valid_count += 1

	if i % 10000 == 0:
		all_boards_iter.set_description(f"{valid_count / (i+1)}")


valid_boards_iter = tqdm(valid_boards)
solutions = []
for board in valid_boards_iter:
	inverse_board = np.logical_not(board)
	if no_squares(inverse_board):
		solutions.append(inverse_board)

print(solutions)
