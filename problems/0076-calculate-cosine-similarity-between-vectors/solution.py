import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	v1 = np.array(v1, dtype=float)
	v2 = np.array(v2, dtype=float)

	a1 = v1.T @ v2
	a2 = (v1.T @ v1)**0.5
	a3 = (v2.T @ v2)**0.5

	return (a1/(a2*a3))

