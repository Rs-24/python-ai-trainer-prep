

class Solution:
    def rotate(self, matrix: list[list]) -> None:
        # Time: O(n^2)
        # Space: O(1)
        n = len(matrix)
        for r in range(n):
            for c in range(r + 1, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        for r in range(n):
            matrix[r].reverse()


