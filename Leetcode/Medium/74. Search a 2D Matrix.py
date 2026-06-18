

class Solution:
    def searchMatrix(self, matrix: list[list], target: int) -> bool:
        # Time: O(log m * n)
        # Space: O(1)
        l, r, n = 0, len(matrix) * len(matrix[0]) - 1, len(matrix[0])
        while l <= r:
            m = (l + r) // 2
            if matrix[m // n][m % n] == target:
                return True
            elif matrix[m // n][m % n] < target:
                l = m + 1
            else:
                r = m - 1
        return False


