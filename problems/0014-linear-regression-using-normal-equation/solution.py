import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	X = np.asarray(X, dtype=float)
	y = np.asarray(y, dtype=float).ravel()
	N = (np.linalg.inv(X.T @ X)) @ (X.T @ y)
	return np.round(N.ravel(), 3).tolist()