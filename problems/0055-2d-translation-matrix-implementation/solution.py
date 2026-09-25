import numpy as np
def translate_object(points, tx, ty):
	# points = np.array(points, dtype=float)
	# T = np.array([tx, ty])
	# translated_points = []
	# for p in points:
	# 	translated_points.append((p+T).tolist())
	# return translated_points

	for p in points:
		p.append(1)

	points = np.array(points, dtype=float)
	T = np.eye(3)

	T[0, -1] = tx
	T[1, -1] = ty

	# print(points[0].shape)
	P = T @ points.T
	
	P = P[:-1,:].T
	
	return P.tolist()


