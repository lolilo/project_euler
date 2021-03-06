# What is the greatest product of four adjacent numbers in the same direction 
# (up, down, left, right, or diagonally) in the 20 x 20 grid?

grid = """
08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"""

# make array of arrays -- matrix
# ennumerate all possiblities and keep track of largest sum in a variable

# create matrix from number strings in a nxn matrix format
def create_matrix(grid, n):
	grid = grid.split() # creates list of num strings
	i = 0
	matrix = []
	row_length = n

	while i < len(grid): # while i < number of rows 
		row = grid[i:i+row_length] # up to but not including row_length index, 0 to row_length - 1
		# convert everything to integers
		for j in xrange(len(row)):
			row[j] = int(row[j])
		
		matrix.append(row) 
		i += row_length

	return matrix

# prod_size = number of ints to multiply together
def greatest_product(matrix, prod_size):

	def greatest_row_product(matrix, prod_size):
		# rows ~ O(n^2)

		greatest_product = 0
		for row in matrix:
			i = 0
			while i <= len(row) - prod_size:
				product = reduce(lambda x, y: x*y, row[i:i+prod_size])

				if product > greatest_product:
					greatest_product = product
				
				product = 1
				i += 1

		return greatest_product

	def greatest_column_product(matrix, prod_size): # O(n^3)
		greatest_product = 0

		for column in xrange(len(matrix[0])):
			product = 1
			i = 0
			i_start = 0
			i_end = i_start + prod_size - 1 # inclusive end
			
			while i_end <= len(matrix[0]) - 1:

				while i <= i_end: # enmerate all products in the column
					# calculate one product
					product *= matrix[i][column]
					i += 1

				if product > greatest_product:
					greatest_product = product

				i = i_start + 1
				i_start = i
				i_end = i_start + prod_size - 1
				product = 1

		return greatest_product

	# diagonal \
	def greatest_right_diagonal(matrix, prod_size):
		greatest_product = 0

		for i in xrange(len(matrix[0])):
			# print 'i is', i
			end = len(matrix[0]) # inclusive end
			i_end = i + prod_size - 1

			while i <= end: # enumerate
				# find product
				product = 1
				while i <= i_end and i < end:
					product *= matrix[i][i]
					i += 1
				
				if product > greatest_product:
					greatest_product = product

				# print 'product is', product
				product = 1
				i += 1
				i_end += 1

		return greatest_product

	# diagonal /
	def greatest_left_diagonal(matrix, prod_size):
		greatest_product = 0

		for row in xrange(len(matrix[0])):
			for x in xrange(len(matrix[row])): # for each element in first row
				# print 'i is', i
				y = row
				x_end = x - prod_size 

				# find each product
				product = 1
				while x > x_end and y < len(matrix[0]):
					# print x, y
					product *= matrix[x][y]
					x -= 1
					y += 1
				
				if product > greatest_product:
					greatest_product = product

				# print 'product is', product
				# print ''
				product = 1

		return greatest_product

	print 'row product: ', greatest_row_product(matrix, prod_size)
	print 'column product: ', greatest_column_product(matrix, prod_size)
	print 'greatest right product: ', greatest_right_diagonal(matrix, prod_size)
	print 'greatest left product: ', greatest_left_diagonal(matrix, prod_size)

	row = greatest_row_product(matrix, prod_size)
	col = greatest_column_product(matrix, prod_size)
	right_diag = greatest_right_diagonal(matrix, prod_size)
	left_diag = greatest_left_diagonal(matrix, prod_size)
	return max(row, col, right_diag, left_diag)

test = """
1 2 3
4 5 6
7 8 9"""

matrix = create_matrix(grid, 20)
print greatest_product(matrix, 4)
