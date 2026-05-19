

class Solution:
    def diagonalSum(self, mat: list[list]) -> int:
        # Time: O(n), n = len(mat)
        # Space: O(1)
        n = len(mat)
        total = 0
        for i in range(n):
            total += mat[i][i] + mat[i][n - i - 1] if i != n - i - 1 else mat[i][i]
        return total


