import numpy as np

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	matrix = np.array(matrix)
	eigvals = np.linalg.eigvals(matrix)
	return eigvals