from check import *


"""
using backtracking to solve sudoku

"""

s=make_sudoku_solution()
b=make_sudoku(s)


def get_empty(b):
	lst=[]
	for r in range(9):
		for c in range(9):
			if not b[r][c]:
				lst.append((r,c))
	return lst

def solve(b):
	if not contain0(b):
		return b

	i=get_empty(b)[0] # the index of tbe box that we are goint to try


	
	
	possible_nums=can_use(b,i[0],i[1])
	if not possible_nums:
		return []

	for n in possible_nums:
		b[i[0]][i[1]]=n
		if solve(b):
			return b

		b[i[0]][i[1]]=0

				





	






	





