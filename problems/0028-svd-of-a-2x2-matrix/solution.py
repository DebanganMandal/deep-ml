import numpy as np
import math

def svd_2x2(A: np.ndarray) -> tuple:
    """
    Compute SVD of a 2x2 matrix.
    
    Args:
        A: 2x2 numpy array
    
    Returns:
        U: 2x2 orthogonal matrix (left singular vectors)
        s: 1D array of singular values
        V: 2x2 matrix (right singular vectors)
    """
    # A = np.asarray(A, dtype=float)
    # assert A.shape == (2, 2)

    # # ------------------------------------------------------------------
    # # 1. Form the Gram matrix B = AᵀA
    # # ------------------------------------------------------------------
    # B = A.T @ A
    # a, c = B[0, 0], B[0, 1]
    # b     = B[1, 1]

    # # ------------------------------------------------------------------
    # # 2. Compute the Jacobi rotation that diagonalizes B
    # # ------------------------------------------------------------------
    # if abs(c) < 1e-15:                     # already diagonal
    #     cth, sth = 1.0, 0.0
    # else:
    #     # tan(2θ) = 2c / (a - b)
    #     tau = (a - b) / (2.0 * c)
    #     # stable computation of t = tan θ
    #     t = np.sign(tau) / (abs(tau) + np.sqrt(1.0 + tau*tau))
    #     cth = 1.0 / np.sqrt(1.0 + t*t)
    #     sth = t * cth

    # # Right singular vectors (columns of V_right)
    # V_right = np.array([[ cth, sth],
    #                     [-sth, cth]])

    # # ------------------------------------------------------------------
    # # 3. Singular values = sqrt of eigenvalues of B
    # # ------------------------------------------------------------------
    # # After the rotation the eigenvalues are on the diagonal of Vᵀ B V
    # lambda1 = a*cth*cth + 2*c*sth*cth + b*sth*sth
    # lambda2 = a*sth*sth - 2*c*sth*cth + b*cth*cth
    # s = np.sqrt(np.maximum([lambda1, lambda2], 0.0))

    # # Sort singular values in descending order and permute V_right accordingly
    # if s[0] < s[1]:
    #     s = s[::-1]
    #     V_right = V_right[:, ::-1]

    # # ------------------------------------------------------------------
    # # 4. Left singular vectors from A V = U Σ
    # # ------------------------------------------------------------------
    # U = A @ V_right
    # for i in range(2):
    #     if s[i] > 1e-14:
    #         U[:, i] /= s[i]
    #     else:
    #         # σ ≈ 0 → choose any unit vector orthogonal to the other column
    #         U[:, i] = np.array([-U[1, 1-i], U[0, 1-i]])
    #         U[:, i] /= np.linalg.norm(U[:, i])

    # # Optional: force det(U) ≈ +1 (proper rotation)
    # if np.linalg.det(U) < 0:
    #     U[:, 1] *= -1
    #     V_right[:, 1] *= -1          # keep A = U Σ Vᵀ consistent

    # # The problem asks for A = U @ diag(s) @ V, therefore return V = V_right.T
    # V = V_right.T

    # return U, s, V

    """
    My Solution
    """

    # B = A.T @ A

    # a = B[0][0]
    # c = B[1][0]
    # b = B[1][1]

    # ev1 = (a+b)/2 + math.sqrt(((a-b)/2)**2 + c**2)
    # ev2 = (a+b)/2 - math.sqrt(((a-b)/2)**2 + c**2)

    # s1, s2 = [math.sqrt(max(ev1, 0)), math.sqrt(max(ev2, 0))]
    # s = [s1, s2]

    # s = np.sort(s)[::-1]

    # if a == b: 
    #     theta = np.pi/4
    # else:
    #     tan_2theta = (2 * c) / (a - b)
    #     theta = 0.5 * np.arctan(tan_2theta)
        
    # V = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
    # V = V[:, np.argsort(s)[::-1]]

    # U = A @ V / s          # broadcasts correctly
    # # then normalize columns if desired
    # U /= np.linalg.norm(U, axis=0)

    # return U, s, V.T

    """
    Another Solution
    """
    return np.linalg.svd(A)