import numpy as np

def phi_transform(data: list[float], degree: int) -> list[list[float]]:
	"""
	Perform a Phi Transformation to map input features into a higher-dimensional space by generating polynomial features.

	Args:
		data (list[float]): A list of numerical values to transform.
		degree (int): The degree of the polynomial expansion.

	"""
	rows = len(data)
	cols = degree+1

	result = np.zeros((rows, cols))

	for r in range(rows):
		result[r] = [data[r]**j for j in range(degree+1)]
	
	return result.tolist()