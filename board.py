from random import *
import random
import requests
from check import *



class Board:
	"""
	Initialize the board with different difficulty
	Level range from 1 to 3
	"""
	def __init__(self, level):
		self.board = [ [0 for row in range(9)] for column in range(9)]
		params = {'size': 9, 'level': level}
		request = requests.get('http://www.cs.utep.edu/cheon/ws/sudoku/new/', params)
		for square in request.json()['squares']:
			self.set_value(square['x'], square['y'], square['value'])


	def print_board(self):
		for i in range(9):
			for j in range(9):
				if j % 3 == 2:
					print(self.board[j][i], end=" |")
				else:
					print(self.board[j][i],end=" ")

			if i % 3 == 2:
				print("\n- - - - - - - - - - - ")
			else:
				print()

	"""
	get the top left cell of the given box
	The order of boxes goes from left to right,
	top to bottom
	123
	456
	789

	"""
	def get_box(self,num):
		if num == 1 or num == 2 or num ==3:
			return(num * 2, 0)
		if num == 4 or num == 5 or num ==6:
			return(num % 3 * 3, 3)

		if num == 7 or num == 8 or num ==9:
			return(num % 3 * 3, 6)

	"""
	set the value to a given cell
	"""
	def set_value(self, x, y, value):
		self.board[x][y] = value

	def get_value(self, x, y):
		return self.board[x][y]

	"""
	Return a list of tuple of empty cells
	Each cell has x and y coordinate
	
	"""
	def empty_cells(self):
		lst = []
		for x in range(9):
			for y in range(9):
				if self.get_value(x, y) == 0:
					lst.append((x, y))

		return lst

	def solve(self):
		empty = self.empty_cells()
		if not empty:
			return True
		else:
			x, y = empty[0]
			for i in range(1, 10):
				if valid(self.board, x, y, i):
					self.set_value(x, y, i)

					if self.solve():
						return True
				self.set_value(x, y, 0)

		return False








