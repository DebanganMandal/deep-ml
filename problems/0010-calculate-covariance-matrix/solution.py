import numpy as np

def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	X = np.array(vectors, dtype=np.float64)
	# First, Find the center point OR mean for each feature point Xi
	# Xi_mean = 1/n * Sum of elements of Xi
	X_mean = np.mean(X, axis=1, keepdims=True)
	# Center the data, which means substract the mean from feature values
	# X_center = Xik - Xi_mean_k
	X_center = X - X_mean
	#  Calculate the Covariance Between Two Features, The covariance between two feature vectors Xi and Xj, measures how they change together.
	n = X.shape[1] # Get number of rows, or here get number of feature points
	cov_matrix = (1/(n-1)) * (X_center @ X_center.T)
	# print(X_center @ X_center.T)
	# for i in range(n):
	# 	for j in range(n):
	# 		cov_matrix[i][j] = (1/(n-1))*(X_center[i] @ X_center[j])
	return cov_matrix.tolist()