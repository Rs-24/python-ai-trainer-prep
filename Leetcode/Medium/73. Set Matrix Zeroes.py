

class Solution:
    def setZeroes(self, matrix: list[list]) -> None:
        # Time: O(m * n)
        # Space: O(1)
        m, n = len(matrix), len(matrix[0])
        r = any(matrix[i][0] == 0 for i in range(m))
        c = any(matrix[0][j] == 0 for j in range(n))
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(n):
                    matrix[i][j] = 0
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(m):
                    matrix[i][j] = 0
        if r:
            for i in range(m):
                matrix[i][0] = 0
        if c:
            for j in range(n):
                matrix[0][j] = 0


