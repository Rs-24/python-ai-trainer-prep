

class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        # Time: O(m * n), m = len(matrix), n = len(matrix[0])
        # Space: O(m * n)
        m, n = len(matrix), len(matrix[0])
        out = [[0] * m for _ in range(n)]
        for r in range(m):
            for c in range(n):
                out[c][r] = matrix[r][c]
        return out


