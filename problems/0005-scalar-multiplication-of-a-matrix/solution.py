import numpy as np

def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	matrix = np.array(matrix)
	res = np.zeros(matrix.shape)

	for i,row in enumerate(matrix):
		res[i] = [x*scalar for x in row]

	return res