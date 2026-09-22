import numpy as np

def make_diagonal(x: np.ndarray):
	n = len(x)
	dig = np.zeros((n,n))

	for i in range(n):
		dig[i][i] = x[i]
	return dig