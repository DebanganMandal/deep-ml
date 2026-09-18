import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	try: 
		b = np.reshape(np.array(a), new_shape)
		reshaped_matrix = b.tolist()
	except ValueError as e:
		reshaped_matrix = []
	return reshaped_matrix