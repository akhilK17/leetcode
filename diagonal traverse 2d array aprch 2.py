class Solution:
	def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:

		# check empty matrix
		
		if not matrix or not matrix[0]:
			return[]

		# dimensions of the matrix
		N,M = len(matrix), len(matrix[0])

		# incides to help progress, one element at a time
		row, column = 0, 0

		# to keep track of direction wheather its up or down

		direction = 1

		# final result array to keep elements of the matrix
		result = []

		#iterate through all the elements

		while row < N and column < M:

			result.append(matrix[row][column])

			new_row = row + (-1 if direction == 1 else -1)
			new_column = column + (1 if direction == 1 else -1)

			if new_row < 0 or new_row == N or new_column < 0 or new_column == M:

				if direction:
					row += (column == M - 1)
					column += (column < M - 1)
				else:
					column += (row == N - 1)
					row += (row < N - 1)

				direction = 1 - direction
			else:
				row = new_row
				column = new_column

		return result