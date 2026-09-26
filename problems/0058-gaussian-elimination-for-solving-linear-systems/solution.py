import numpy as np

def gaussian_elimination(A, b):
	"""
	Solves the system Ax = b using Gaussian Elimination with partial pivoting.
    
	:param A: Coefficient matrix
	:param b: Right-hand side vector
	:return: Solution vector x
	"""
	A = np.asarray(A, dtype=float)
	b = np.asarray(b, dtype=float)
	A_b = np.zeros((A.shape[0], A.shape[1]+1))

	# Create Augmented Matrix
	A_b[:, :-1] = A
	A_b[:, -1] = b

	# Create Upper Triangular Matrix
	rows = A_b.shape[0]
	cols = A_b.shape[1]
	pivot_row = 0

	row = 0

	for col in range(cols):
		pivot_row = row
		max_pivot = abs(A_b[row, col])

		for r in range(row+1, rows):
			if max_pivot < abs(A_b[r, col]):
				max_pivot = abs(A_b[r, col])
				pivot_row = r
				# break
		# pivot_row = row + np.argmax(np.abs(A_b[col:, col]))

		A_b[[row, pivot_row]] = A_b[[pivot_row, row]]

		for r in range(row+1, rows):
			A_b[r] = A_b[r] - (A_b[r, col]*A_b[row])/A_b[row, col]

		row += 1
		if row >= rows:
			break
	

	n = rows
	x = np.zeros(n)
	for i in range(n-1, -1, -1):
		s = A_b[i, i+1:n] @ x[i+1:n]
		x[i] = (A_b[i, -1] - s) / A_b[i, i]
		
	return np.round(x, 6).tolist()