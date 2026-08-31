

class Solution:
    def countSquares(self, matrix: list) -> int:
        # Time: O(m * n)
        # Space: O(1)
        m, n = len(matrix), len(matrix[0])
        ans = 0
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 1 and r > 0 and c > 0:
                    matrix[r][c] += min(matrix[r - 1][c], matrix[r][c - 1], matrix[r - 1][c - 1])
                ans += matrix[r][c]
        return ans


