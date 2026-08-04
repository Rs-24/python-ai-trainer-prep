

class Solution:
    def minFallingPathSum(self, matrix: list) -> int:
        # Time: O(n^2)
        # Space: O(1)
        n = len(matrix)
        for r in range(1, n):
            for c in range(n):
                t = matrix[r - 1][c]
                if c > 0:
                    t = min(t, matrix[r - 1][c - 1])
                if c < n - 1:
                    t = min(t, matrix[r - 1][c + 1])
                matrix[r][c] += t
        return min(matrix[-1])


        