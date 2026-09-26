import numpy as np

def gauss_seidel(A, b, n, x_ini=None):
	# A = np.array(A, dtype=float)
	# b = np.array(b, dtype=float)
	# # #rows = #cols = p
	# p = A.shape[0]
	# if x_ini is None:
	# 	x_ini = np.zeros(p)
	# else:
	# 	x = np.asarray(x_ini, dtype=float).ravel().copy()
	# x_new = np.zeros_like(x_ini)
	# x_new = x = x_ini

	# for c in range(n):
	# 	for i in range(p):
	# 		S1 = sum(A[i][j]*x_new[j] for j in range(i))
	# 		S2 = sum(A[i][j]*x[j] for j in range(i+1, p))
	# 		x_new[i] = (1/A[i, i])*(b[i] - S1 - S2)
	# 	x = x_new

	# return np.round(x, 4).tolist()

	A = np.array(A, dtype=float)
	b = np.array(b, dtype=float)
	p = A.shape[0]

	if x_ini is None:
		x = np.zeros(p)
	else:
		x = np.array(x_ini, dtype=float)

	for _ in range(n):
		for i in range(p):
			s1 = A[i, :i] @ x[:i]
			s2 = A[i, i+1:] @ x[i+1:]
			x[i] = (b[i] - s1 - s2)/A[i, i]

	return np.round(x, 4).tolist()