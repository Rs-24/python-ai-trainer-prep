

class Solution:
    def searchMatrix(self, matrix: list[list], target: int) -> bool:
        # Time: O(m + n)
        # Space: O(1)
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        r, c = 0, n - 1
        while r < m and c >= 0:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                r += 1
            else:
                c -= 1
        return False


