
import random

def check_column(b,r,c):
	# check the numbers that haven't been used in one column
	lst=list(range(1,10))
	for i in range(9):
		if b[c][i]:
			lst.remove(b[c][i])

	return lst


def check_row(b,r,c):
	lst=list(range(1,10))
	for i in range(9):
		if b[i][r]:
			lst.remove(b[i][r])

	return lst

def check_board(b,r,c):
	"""
	block start index represents the index of the left top small box 
	"""
	block_start_index_r=r//3*3
	block_start_index_c=c//3*3

	lst=list(range(1,10))
	for i in range(3):
		for j in range(3):
			if b[block_start_index_r+i][block_start_index_c+j]:
				lst.remove(b[block_start_index_r+i][block_start_index_c+j])


	return lst

def can_use(b,r,c):
	if b[r][c]:
		return []
	set_a=check_column(b,r,c)
	set_b=check_row(b,r,c)
	set_c=check_board(b,r,c)
	lst=list(set(set_a).intersection(set_b).intersection(set_c))
	return lst
def contain0(b):
	for i in range(9):
		if 0 in b[i]:
			return True
	return False

def make_sudoku_solution():

	def helper():
		b=[ [0 for r in range(9)] for c in range(9)]
		for i in range(9):
			for j in range(9):
				try:
					n=random.choice(can_use(b,i,j))
					b[i][j]=n
				except IndexError:
					b[i][j]=0
		return b

	b=helper()
	while contain0(b):
		b=helper()
	return b


def print_board(b):
	for i in range(9):
		for j in range(9):
			print(b[i][j],end=" ")

		print(" ")

def make_sudoku(b,level="easy"):
	"""
	empty some boxes in the solution

	"""
	copy_b=[row[:] for row in b]
	count=40
	while count:
		r=choice(range(9))
		c=choice(range(9))

		if copy_b[r][c]:
			copy_b[r][c]=0
			count-=1

	return copy_b








