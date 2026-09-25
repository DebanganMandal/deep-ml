import numpy as np

def rref(matrix):
	
	A = np.array(matrix, dtype=float)

	rows, cols = A.shape[0], A.shape[1]
	row = 0

	for col in range(cols):
		# If the pivot element is 0, then Find the next row with non zero entry in the later rows, and if you find any, swap the current row with the new row
		pivot_row = None
		for r in range(row, rows):
			if A[r, col] != 0:
				pivot_row = r
				break

		# pivot_row is -1, means that column has not non zero elements in the pivot column, so let the row be.
		if pivot_row == None:
			continue

		# Swap the row and pivot_row
		if pivot_row is not None:
			A[[row, pivot_row]] = A[[pivot_row, row]]


		# Scaling the whole row, so that A[i][i] [pivot element is 1]
		A[row] /= A[row][col]

		# Now every other row, other than the row of the pivot element is to be reduced, all the column as the pivot element to be reduced to 0, operatin required: Rj = Rj - Aji*Ri
		for r in range(rows):
			if r != row:
				A[r] -= A[r, col]*A[row]

		row += 1
		if row == rows:
			break

	return A.tolist()