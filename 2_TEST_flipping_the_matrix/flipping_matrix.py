#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#
def flippingMatrix(mat):
    n = len(mat) // 2
    Sum = 0
    for i in range(0, n):
        for j in range(0, n):
        
            r1, r2 = i, 2*n - i - 1
            c1, c2 = j, 2*n - j - 1
    
            Sum += max(max(mat[r1][c1], mat[r1][c2]),
            max(mat[r2][c1], mat[r2][c2]))
    return Sum