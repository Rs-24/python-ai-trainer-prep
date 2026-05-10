

class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        # Time: O(m * n), m = len(matrix), n = len(matrix[0])
        # Space: O(1)
        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                if matrix[r - 1][c - 1] != matrix[r][c]:
                    return False
        return True


