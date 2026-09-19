import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
	v = A.shape[1]
	x = np.zeros((v,))

	for c in range(n):
		x_new = np.zeros_like(x)
		for i in range(v):
			s = sum(A[i][j] * x[j] for j in range(v) if j!=i)
			x_new[i] = (1/A[i][i])*(b[i] - s)
		x = x_new
	return np.round(x, 4).tolist()