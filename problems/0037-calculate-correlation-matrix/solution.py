import numpy as np

def calculate_correlation_matrix(X: np.ndarray, Y: np.ndarray = None) -> np.ndarray:
    # If Y is not provided, compute correlation of X with itself
    if Y is None:
        Y = X

    # Ensure float type
    X = np.asarray(X, dtype=float)
    Y = np.asarray(Y, dtype=float)

    # Number of observations
    n = X.shape[0]

    # Center the data (subtract column means)
    X_centered = X - X.mean(axis=0)
    Y_centered = Y - Y.mean(axis=0)

    # Compute standard deviations (sample version, ddof=1)
    std_X = X_centered.std(axis=0, ddof=1)
    std_Y = Y_centered.std(axis=0, ddof=1)

    # Avoid division by zero
    std_X[std_X == 0] = 1.0
    std_Y[std_Y == 0] = 1.0

    # Correlation matrix = (X_c.T @ Y_c) / ((n-1) * outer(std_X, std_Y))
    corr = (X_centered.T @ Y_centered) / ((n - 1) * np.outer(std_X, std_Y))

    return corr