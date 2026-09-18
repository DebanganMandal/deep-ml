import numpy as np

def row_wise_sum(matrix:np.ndarray):
	means = []
	for row in matrix:
		s = 0
		for n in row:
			s += n
		means.append(s)
	return means

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	means = []
	m = len(matrix)
	n = len(matrix[0])

	matrix = np.array(matrix)

	if mode == "row": 
		means = row_wise_sum(matrix)
		means = [x/n for x in means]
	else: 
		means = row_wise_sum(matrix.T)
		means = [x/m for x in means]

	return means