import numpy as np

def compressed_row_sparse_matrix(dense_matrix):
	"""
	Convert a dense matrix to its Compressed Row Sparse (CSR) representation.

	:param dense_matrix: 2D list representing a dense matrix
	:return: A tuple containing (values array, column indices array, row pointer array)
	"""
	X = np.asarray(dense_matrix, dtype=float)
	rows, cols = X.shape
	row_ptr = np.zeros(rows + 1)


	# vals = X[X != 0].ravel().tolist()
	p = [(j, val) for row in dense_matrix for j, val in enumerate(row) if val!=0]

	col_idx, vals = zip(*p)

	for i in range(rows):
		row_ptr[i+1] = row_ptr[i] + np.sum(X[i]!=0)

	return list(vals), list(col_idx), row_ptr.astype(int).tolist()
