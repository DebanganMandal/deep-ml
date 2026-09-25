import numpy as np
def translate_object(points, tx, ty):
	points = np.array(points, dtype=float)
	T = np.array([tx, ty])
	translated_points = []
	for p in points:
		translated_points.append((p+T).tolist())
	return translated_points
