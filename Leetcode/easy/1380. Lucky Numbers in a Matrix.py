

class Solution:
    def luckyNumbers(self, matrix: list[list]) -> list:
        # Time: O(m * n), m = len(matrix), n = len(matrix[0])
        # Space: O(m + n)
        row = [min(r) for r in matrix]
        col = [max(c) for c in zip(*matrix)]
        return [matrix[r][c]
                for r in range(len(matrix))
                for c in range(len(matrix[0]))
                if matrix[r][c] == row[r] and matrix[r][c] == col[c]]


