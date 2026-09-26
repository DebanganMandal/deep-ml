import numpy as np

def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):

	# Find Mean across the column/feature
	means = np.mean(data, axis=0, keepdims=True)
	std = np.std(data, axis=0, keepdims=True)

	standardized_data = [np.round((d - means)/std, 4).ravel().tolist() for d in data]

	min_val = np.min(data, axis=0, keepdims=True)
	max_val = np.max(data, axis=0, keepdims=True)
	diff = max_val - min_val

	normalized_data = [np.round((d - min_val)/diff, 4).ravel().tolist() for d in data]

	return standardized_data, normalized_data