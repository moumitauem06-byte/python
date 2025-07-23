def printSpiral(mat):
    while mat:
        print(*mat.pop(0), end=' ')
        if mat and mat[0]:
            for row in mat:
                print(row.pop(), end=' ')
        if mat:
            print(*mat.pop()[::-1], end=' ')
        if mat and mat[0]:
            for row in mat[::-1]:
                print(row.pop(0), end=' ')

# Example usage:
mat = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12], 
       [13, 14, 15, 16]]

printSpiral(mat)
