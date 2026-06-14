

class Solution:
    def modifiedMatrix(self, matrix: list[list]) -> list[list]:
        # Time: O(n^2)
        # Space: O(n)
        m = []
        for c in range(len(matrix[0])):
            b = float("-inf")
            for r in range(len(matrix)):
                if matrix[r][c] != -1:
                    b = max(b, matrix[r][c])
            m.append(b)
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == -1:
                    matrix[r][c] = m[c]
        return matrix


