import numpy as np
import math as m

# def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
# 	matrix = np.array(matrix)
# 	eigvals = np.linalg.eigvals(matrix)
# 	return eigvals

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	a, b = matrix[0][0], matrix[0][1]
	c, d = matrix[1][0], matrix[1][1]

	T = a + d
	D = a*d - b*c

	ev1 = (T + m.sqrt(T**2 - 4*D))/2
	ev2 = (T - m.sqrt(T**2 - 4*D))/2

	return [ev1, ev2]