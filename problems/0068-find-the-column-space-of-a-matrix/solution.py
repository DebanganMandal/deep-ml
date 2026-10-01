
import numpy as np

def matrix_image(X):
	X = np.asarray(X, dtype=float)
	A = X.copy()
	# A = A.T
	rank = np.linalg.matrix_rank(A)
	r = 0

	rows, cols = A.shape

	row = 0

	for col in range(cols):
		for r in range(row+1, rows):
			if A[r, col] != 0:
				A[r] = A[row, col]*A[r] -  A[r, col]*A[row]
		row += 1
		if row == rows:
			break
	
	# print(A)
	idx = -1
	
	for row in A:
		if np.sum(row!=0)>0:
			idx += 1

	if idx == -1:
		return X
	
	return X[:,:idx+1]