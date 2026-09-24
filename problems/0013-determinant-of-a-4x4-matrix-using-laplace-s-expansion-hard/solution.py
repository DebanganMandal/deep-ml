import numpy as np

def determinant_3X3(matrix: np.ndarray) -> float:
	a1, b1, c1 = matrix[0][0], matrix[0][1], matrix[0][2]
	a2, b2, c2 = matrix[1][0], matrix[1][1], matrix[1][2]
	a3, b3, c3 = matrix[2][0], matrix[2][1], matrix[2][2]

	return (
		a1 * (b2*c3 - b3*c2)
		- b1* (a2*c3 - c2*a3)
		+ c1 * (a2*b3 - b2*a3)
	)

def determinant_4x4(matrix: list[list[int|float]]) -> float:
	A = np.array(matrix, dtype=float)
	S = 0
	rows = [1, 2, 3]
	cols = []

	for i in range(4):
		cols = [c for c in range(A.shape[1]) if c!=i]
		M = A[np.ix_(rows, cols)]

		S += (-1)**(0+i) * A[0][i] * determinant_3X3(M)

	return S