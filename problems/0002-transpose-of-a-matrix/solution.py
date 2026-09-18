def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    m = len(a)
    n = len(a[0])
    # initialize the result 2D matrix of shape (m,n)
    res = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(m):
        for j in range(n):
            res[j][i] = a[i][j]

    return res