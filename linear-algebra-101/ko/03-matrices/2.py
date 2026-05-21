"""Generated from book-content article."""

A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])

C = A @ B

# 수동 계산 확인
c00 = np.dot(A[0, :], B[:, 0])
c01 = np.dot(A[0, :], B[:, 1])
c10 = np.dot(A[1, :], B[:, 0])
c11 = np.dot(A[1, :], B[:, 1])

C_manual = np.array([[c00, c01],
                     [c10, c11]])

print('C:', C)
print('C_manual:', C_manual)
print('same?', np.allclose(C, C_manual))
