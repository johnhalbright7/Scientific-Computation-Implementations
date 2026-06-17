import numpy as np

def gram_schmidt(A: np.typing.NDArray):
    v = np.zeros(A.shape)
    v[:,0] = A[:,0]
    Q = np.zeros(A.shape)
    for i in range(1, A.shape[1]): # For each column in A
        Q[:,[i-1]] = v[:,[i-1]] / np.linalg.norm(v[:,[i-1]])
        v[:,[i]] = A[:,[i]]
        for j in range(0, i):
            v[:,[i]] -= ((Q[:, [j]] @ Q[:,[j]].T) @ A[:,[i]])
    last_col = A.shape[1]-1
    Q[:,[last_col]] = v[:,[last_col]] / np.linalg.norm(v[:,[last_col]])
    R = np.zeros(A.shape)
    for row in range(0, R.shape[0]):
        R[row, row] = np.linalg.norm(v[:,[row]])
        for col in range(row+1, R.shape[1]):
            R[row, col] = Q[:,row].T @ A[:,col]


    return Q, R


A = np.array([[1, 2, 3],
              [2, 2, 2],
              [3, 2, 3]])

Q, R = gram_schmidt(A)
print(Q)
print(R)
print(Q @ R)