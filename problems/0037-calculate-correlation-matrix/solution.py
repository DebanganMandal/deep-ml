import numpy as np

def calculate_correlation_matrix(X, Y=None):
	if Y is None: Y = X

	X = np.array(X, dtype=float)
	Y = np.array(Y, dtype=float)

	Xc = X - np.mean(X, axis=0, keepdims=True)
	Yc = Y - np.mean(Y, axis=0, keepdims=True)

	X_std = Xc.std(axis=0, ddof=1)
	Y_std = Yc.std(axis=0, ddof=1)

	X_std[X_std==0] = 1.0
	Y_std[Y_std==0] = 1.0
	
	n = X.shape[0]

	corr = (Xc.T @ Yc) / ((n - 1) * np.outer(X_std, Y_std))

	return corr